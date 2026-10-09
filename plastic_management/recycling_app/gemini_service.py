
import os
import json
from io import BytesIO

from dotenv import load_dotenv
from google import genai
from PIL import Image


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)


def identify_waste(image_file):
    """Identify multiple visible waste items using Gemini Vision."""

    image_file.seek(0)
    image = Image.open(BytesIO(image_file.read())).convert("RGB")

    prompt = """
    Analyze this image for a waste management system.

    Identify the different visible waste items. Do not identify only
    the largest item. Group similar items when appropriate.

    Return ONLY valid JSON with this structure:

    {
      "items": [
        {
          "name": "Plastic bottle",
          "material": "Plastic",
          "polymer": "PET",
          "confidence": 90,
          "recyclable": true,
          "reason": "A bottle that appears to be made from PET plastic."
        }
      ],
      "summary": "Multiple plastic items are visible.",
      "overall_material": "Plastic"
    }

    Rules:
    - Include each distinct visible waste item or item category.
    - Do not invent objects that are not visible.
    - Use "Unknown" if the material or polymer cannot be determined.
    - Polymer can be PET, HDPE, PVC, LDPE, PP, PS, Other or Unknown.
    - Do not guess a precise polymer from appearance alone.
    - Confidence must be a number from 0 to 100.
    - Recyclable must be true, false or null.
    - Use null when recyclability cannot be determined.
    - Recyclability depends on material, contamination and local facilities.
    - Do not claim that every item is recyclable just because it is plastic.
    - Do not include Markdown code fences.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt, image],
    )

    response_text = response.text

    if not response_text:
        raise ValueError("Gemini returned an empty response.")

    response_text = response_text.strip()

    if response_text.startswith("```"):
        response_text = response_text.split("\n", 1)[1]
        response_text = response_text.rsplit("```", 1)[0].strip()

    data = json.loads(response_text)

    if not isinstance(data.get("items"), list) or not data["items"]:
        raise ValueError("Gemini did not return any identifiable waste items.")

    cleaned_items = []

    for item in data["items"]:
        if not isinstance(item, dict):
            continue

        name = str(item.get("name", "Unknown"))[:100]
        material = str(item.get("material", "Unknown"))[:100]
        polymer = str(item.get("polymer", "Unknown"))[:30]
        reason = str(item.get("reason", ""))

        try:
            confidence = float(item.get("confidence", 0))
        except (TypeError, ValueError):
            confidence = 0

        if not 0 <= confidence <= 100:
            confidence = 0

        recyclable = item.get("recyclable")

        if not isinstance(recyclable, bool):
            recyclable = None

        cleaned_items.append({
            "name": name,
            "material": material,
            "polymer": polymer,
            "confidence": confidence,
            "recyclable": recyclable,
            "reason": reason,
        })

    if not cleaned_items:
        raise ValueError("No valid waste items were returned.")

    # Preserve the existing database fields.
    waste_types = list(dict.fromkeys(
        item["name"] for item in cleaned_items
    ))

    materials = list(dict.fromkeys(
        item["material"] for item in cleaned_items
    ))

    confidences = [item["confidence"] for item in cleaned_items]

    # Overall recyclability is known only if every item has
    # the same known recyclable status.
    recyclable_values = {item["recyclable"] for item in cleaned_items}

    if recyclable_values == {True}:
        overall_recyclable = True
    elif recyclable_values == {False}:
        overall_recyclable = False
    else:
        overall_recyclable = None

    result = {
        "summary": str(data.get("summary", "")),
        "overall_material": str(
            data.get("overall_material", ", ".join(materials))
        ),
        "items": cleaned_items,
    }

    return {
        "waste_type": ", ".join(waste_types)[:100],
        "material": ", ".join(materials)[:100],
        "confidence": round(sum(confidences) / len(confidences), 2),
        "recyclable": overall_recyclable,
        "result": json.dumps(result, ensure_ascii=False),
    }
