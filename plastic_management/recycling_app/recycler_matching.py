
import json
from decimal import Decimal, InvalidOperation

from .models import unit_register_tb


def normalize(value):
    """Normalize text for case-insensitive matching."""
    return str(value or "").strip().lower()


def get_waste_items(waste):
    """
    Extract individual items from Gemini's saved JSON result.
    Fall back to the overall waste fields for older records.
    """
    if waste.ai_result:
        try:
            result = json.loads(waste.ai_result)

            if isinstance(result, dict):
                items = result.get("items", [])

                if isinstance(items, list) and items:
                    return [
                        item for item in items
                        if isinstance(item, dict)
                    ]

        except (json.JSONDecodeError, TypeError):
            pass

    # Fallback for older reports
    if waste.ai_waste_type or waste.ai_material:
        return [{
            "name": waste.ai_waste_type or "Unknown",
            "material": waste.ai_material or "",
            "recyclable": waste.ai_recyclable,
            "confidence": waste.ai_confidence,
        }]

    return []


def item_is_recyclable(item):
    """Only match items explicitly marked recyclable by the AI."""
    return item.get("recyclable") is True


def get_waste_quantity(waste):
    """Return a valid positive waste quantity in kilograms."""
    quantity = waste.waste_quantity_kg

    if quantity is None:
        return None

    try:
        quantity = Decimal(str(quantity))

        if not quantity.is_finite() or quantity <= 0:
            return None

        return quantity

    except (InvalidOperation, TypeError, ValueError):
        return None


def get_recycler_capacity(recycler):
    """Return a valid non-negative recycler capacity in kilograms."""
    try:
        capacity = Decimal(str(recycler.available_capacity_kg))

        if not capacity.is_finite() or capacity < 0:
            return None

        return capacity

    except (InvalidOperation, TypeError, ValueError):
        return None


def find_matching_recyclers(waste):
    """
    Return approved, available recyclers matching:
    1. Waste report district
    2. At least one recyclable AI-detected item
    3. Recycler accepted waste types
    4. Sufficient available capacity for the reported quantity

    A report without a valid quantity will not produce matches.
    """
    district = normalize(waste.district)
    quantity = get_waste_quantity(waste)

    # Capacity cannot be validated without a quantity.
    if not district or quantity is None:
        return []

    items = get_waste_items(waste)

    recyclable_items = [
        item for item in items
        if item_is_recyclable(item)
    ]

    if not recyclable_items:
        return []

    recyclers = unit_register_tb.objects.filter(
        status="approved",
        is_available=True,
    )

    matches = []

    for recycler in recyclers:

        # 1. Validate district
        recycler_district = normalize(
            recycler.district or recycler.place
        )

        if recycler_district != district:
            continue

        # 2. Validate available capacity
        capacity = get_recycler_capacity(recycler)

        if capacity is None or capacity < quantity:
            continue

        # 3. Read accepted waste types
        accepted_types = recycler.accepted_waste_types or []

        if isinstance(accepted_types, str):
            try:
                parsed_types = json.loads(accepted_types)

                accepted_types = (
                    parsed_types
                    if isinstance(parsed_types, list)
                    else [accepted_types]
                )

            except (json.JSONDecodeError, TypeError):
                accepted_types = [accepted_types]

        accepted_types = [
            normalize(value)
            for value in accepted_types
            if normalize(value)
        ]

        if not accepted_types:
            continue

        # 4. Match individual recyclable waste items
        matched_items = []

        for item in recyclable_items:
            item_name = normalize(item.get("name"))
            material = normalize(item.get("material"))
            polymer = normalize(item.get("polymer"))

            item_terms = [
                term
                for term in (material, item_name, polymer)
                if term
            ]

            item_matches = any(
                accepted == term
                or accepted in term
                or term in accepted
                for accepted in accepted_types
                for term in item_terms
            )

            if item_matches:
                matched_items.append(item)

        # Add recycler only if all required conditions pass
        if matched_items:
            matches.append({
                "recycler": recycler,
                "matched_items": matched_items,
                "waste_quantity_kg": quantity,
                "capacity_kg": capacity,
                "remaining_capacity_kg": capacity - quantity,
            })

    return matches
