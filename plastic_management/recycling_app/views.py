from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from datetime import date
from datetime import datetime
from .gemini_service import identify_waste
from .models import register_tb,unit_register_tb,waste_location_tb,feedback_tb,workers_register_tb,product_tb,cart_tb,order_tb,order_item_tb
from django.views.decorators.cache import cache_control
# Create your views here.
import json
from decimal import Decimal
from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .recycler_matching import find_matching_recyclers
#----------------------------------user functions---------------------------------

def home(request):
	return render(request,'user/index.html')

def index(request):
	return render(request,'user/home.html')

def user_login(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["psw"]
		# print(password)
		chk=register_tb.objects.filter(email=email,password=password,status="approved")
		# print(chk)
		if chk:
			for x in chk:
				request.session['id']=x.id
			return render(request,'user/index.html')
		else:
			return render(request,'user/login.html',{'error':'Invalid email id/Password or your request is not accepted'})
	else:
		return render(request,'user/login.html')

def user_registration(request):
	if request.method=="POST":
		name=request.POST["Username"]
		email=request.POST["email"]
		password=request.POST["psw"]
		confimpassword=request.POST["cnfpsw"]
		gender=request.POST["gender"]
		address=request.POST["adss"]
		mobile=request.POST["pno"]
		place=request.POST["place"]
		aadhar=request.POST["adr"]

		chk=register_tb.objects.all().filter(email=email,password=password)
		if chk:
			return render(request,'user/registraion.html',{'error':'Email Already exists'})
		else:
			a=register_tb(name=name,Aadhar_Number=aadhar,email=email,password=password,gender=gender,address=address,mobile_Number=mobile,place=place,status="pending")
			a.save()
			return render(request,'user/home.html',{'success':'successfully registerd'})
	else:
		return render(request,'user/registraion.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_waste_location(request):
	if request.session.has_key('id'):
		if request.method=='POST':
			ii=request.session['id']
			uid=register_tb.objects.all().get(id=ii)
			subject=request.POST["sub"]
			description=request.POST["des"]
			address=request.POST["adss"]
			district=request.POST["district"]
			place=request.POST["place"]
			a=waste_location_tb(user_id=uid,subject=subject,place=place,description=description,address=address,district=district,status="pending")
			a.save()
			return HttpResponseRedirect('/home/')
		else:
			return render(request,'user/add_waste_locations.html')
	else:
		return render(request,'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def profile(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		aa=register_tb.objects.all().filter(id=ii)
		# bb=order_item_tb.objects.all().filter(user_id=ii)
		# print("______________________________________",bb)
		return render(request,'user/user_profile.html',{'db':aa})
	else:
		return render(request,'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def my_order(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		# aa=register_tb.objects.all().filter(id=ii)
		bb=order_item_tb.objects.all().filter(user_id=ii)
		# print("______________________________________",bb)
		return render(request,'user/my_orders.html',{'db':bb})
	else:
		return render(request,'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def shop(request):
	if request.session.has_key('id'):
		var=product_tb.objects.all()
		return render(request,'user/products.html',{'db':var})
	else:
		return render(request,'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def feedback(request):
	if request.session.has_key('id'):
		if request.method=="POST":
			ii=request.session['id']
			uid=register_tb.objects.all().get(id=ii)
			oid=request.POST["pid"]
			var=order_item_tb.objects.all().filter(id=oid)
			print("__________________",var)
			for x in var:
				proid=x.product_id.id
				uniid=x.unit_id.id
			pid=product_tb.objects.all().get(id=proid)
			unid=unit_register_tb.objects.all().get(id=uniid)


			description=request.POST["commet"]
			a=feedback_tb(user_id=uid,product_id=pid,unit_id=unid,feedback=description)
			a.save()
			return HttpResponseRedirect('/my_order/')
		else:
			ii=request.GET['id']
		# var=product_tb.objects.all()
			return render(request,'user/feedback.html',{'pid':ii})
	else:
		return render(request,'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def product_detail_view(request):
	if request.session.has_key('id'):
		aa=request.GET['id']
		pid=product_tb.objects.all().filter(id=aa)
		print(pid)
		return render(request,'user/product_details.html',{'db':pid})
	else:
		return render(request,'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_to_cart(request):
	if request.session.has_key('id'):
		aa=request.GET['id']
		print(aa)
		pid=product_tb.objects.get(id=aa)
		ii=request.session['id']
		uid=register_tb.objects.get(id=ii)
		quantity=request.GET["number"]
		print(quantity)
		unitid=int(pid.unitid.id)
		print("__________________________",unitid)
		unid=unit_register_tb.objects.get(id=unitid)


		aq=int(pid.quantity)
		qu=int(quantity)
		if(aq<qu):
			return render(request,'frontend/product_details.html',{'error':"Requested Quantity is Not Available"})
		else:
			proprice=(pid.price)
			total=int(proprice)*int(quantity)
			var=cart_tb(user_id=uid,product_id=pid,unit_id=unid,quantity=quantity,total=total,status="unpaid")
			print("-----",var)
			var.save()
			return HttpResponseRedirect('/shop/')
	else:
		return render(request,'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cart(request):
	if request.session.has_key('id'):
		ii=request.session["id"]
		tid=cart_tb.objects.all().filter(user_id=ii,status="unpaid")
		print("_____________________________",tid)
		sum1=0
		for x in tid:
			a=x.total
			sum1=sum1+int(a)
			print(sum1)
		return render(request,'user/cart.html',{'db':tid,'sum':sum1})
	else:
		return render(request,'user/login.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def delete_cart(request):
	if request.session.has_key('id'):
		uu=request.session["id"]
		ii=request.GET["id"]
		print("--------ii=====",ii)
		tid=cart_tb.objects.all().filter(id=ii,user_id=uu)
		print("------------------------tid----------------",tid)
		tid.delete()
		return HttpResponseRedirect('/usercart/')
	else:
		return render(request,'user/login.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def payment(request):
    if request.session.has_key('id'):
        if request.method == "POST":
            return HttpResponseRedirect('/shop/')
        else:
            user_id = request.session["id"]
            user = register_tb.objects.filter(id=user_id)
            return render(request, 'user/payment.html', {'db': user})
    else:
        return render(request, 'user/login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_cart_product_payment(request):
    if request.session.has_key('id'):
        if request.method == "POST":
            user_id = request.session["id"]
            unpaid_cart_items = cart_tb.objects.filter(user_id=user_id, status="unpaid")
            uid = register_tb.objects.get(id=user_id)
            amount = request.POST.get("subtotal", 0)
            current_date = date.today()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            cart_ids = []
            unit_ids = []
            product_ids = []

            for item in unpaid_cart_items:
                product_ids.append(item.product_id.id)
                cart_ids.append(item.id)
                unit_ids.append(item.unit_id.id)

            # Create order
            order = order_tb(
                cart_id=cart_ids,
                unit_id=unit_ids,
                user_id=uid,
                product_id=product_ids,
                payment=amount,
                date=current_date,
                time=current_time,
                payment_status="paid",
                status="pending"
            )
            order.save()

            latest_order = order_tb.objects.latest("id")

            # Create order items
            for item in unpaid_cart_items:
                pid = product_tb.objects.get(id=item.product_id.id)
                unid = unit_register_tb.objects.get(id=item.unit_id.id)
                cid = cart_tb.objects.get(id=item.id)
                order_item = order_item_tb(
                    cart_id=cid,
                    unit_id=unid,
                    order_id=latest_order,
                    user_id=uid,
                    product_id=pid,
                    total=amount,
                    date=current_date,
                    time=current_time,
                    payment_status="paid",
                    status="pending"
                )
                order_item.save()

            # Mark cart items as paid
            unpaid_cart_items.update(status="paid")

            return HttpResponseRedirect('/payment/')
    else:
        return render(request, 'user/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def product_booking(request):
	if request.session.has_key('id'):
		ii=request.session["id"]
		uid=register_tb.objects.get(id=ii)
		tid1=request.GET["id"]
		pid=product_tb.objects.get(id=tid1)
		quantity=request.POST["number"]
		print(quantity)
		current_date=date.today()
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		user=register_tb.objects.all().filter(id=ii)
		product=product_tb.objects.all().filter(id=tid1)

		arr=[]
		arr.append(tid1)
		for x in product:
			aqu=(x.quantity)
			ppp=(x.unitid.id)
			uniid=int(ppp)
			aqu=int(aqu)
			qu=int(quantity)
			proprice=(x.price)
			price=int(proprice)*int(quantity)
			Uid=unit_register_tb.objects.get(id=uniid)

			if aqu<qu:
				return render(request,'user/product_details.html',{'error':"Requested Quantity is Not Available"})
			else:
				car=cart_tb(user_id=uid,product_id=pid,unit_id=Uid,quantity=quantity,total=price,status="unpaid")
				car.save()
				var1=cart_tb.objects.latest("id")
				print("_-------------cartid-------------",var1)


				for x in product:
					proprice=(x.price)
					price=int(proprice)*int(quantity)
					a = order_tb(unit_id=uniid,user_id=uid,product_id=tid1,payment=price,date=current_date,time=current_time,payment_status="paid",status="pending")
					a.save()
				arr.pop()
				var=order_tb.objects.latest("id")
				print("_--------------------------",var)
				c = order_item_tb(cart_id=var1,unit_id=Uid,order_id=var,user_id=uid,product_id=pid,total=price,date=current_date,time=current_time,payment_status="paid",status="pending")
				c.save()
				proid=cart_tb.objects.all().filter(user_id=ii).update(status="paid")
				return HttpResponseRedirect('/payment/')
	else:
		return render(request,'user/login.html')



#-------------------------admin functions-----------------------------------------

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def admin_home(request):
	if request.session.has_key('id'):
		return render(request,'admin/index.html')
	
def admin_login(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["password"]
		# print(password)
		chk=User.objects.filter(email=email,password=password)
		# print(chk)
		if chk:
			for x in chk:
				request.session['id']=x.id
			return render(request,'admin/index.html')
		else:
			return render(request,'admin/login.html')
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def user_approval(request):
	if request.session.has_key('id'):
		var=register_tb.objects.all().filter(status="pending")
		return render(request,'admin/users_approval.html',{'db':var})
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def approved_user_list(request):
	if request.session.has_key('id'):
		var=register_tb.objects.all().filter(status="approved")
		return render(request,'admin/approved_users.html',{'db':var})
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def approved_unit_list(request):
	if request.session.has_key('id'):
		var=unit_register_tb.objects.all().filter(status="approved")
		return render(request,'admin/approved_unit.html',{'db':var})
	else:
		return render(request,'admin/login.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def rejected_user_list(request):
	if request.session.has_key('id'):
		var=register_tb.objects.all().filter(status="rejected")
		return render(request,'admin/rejected_user.html',{'db':var})
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def rejected_unit_list(request):
	if request.session.has_key('id'):
		var=unit_register_tb.objects.all().filter(status="rejected")
		return render(request,'admin/rejected_unit.html',{'db':var})
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def approve_user(request):
	if request.session.has_key('id'):
		ii=request.GET["id"]
		fromform=register_tb.objects.all().filter(id=ii).update(status="approved")
		return HttpResponseRedirect('/user_approval/')
	else:
		return render(request,'admin/login.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def reject_user(request):
	if request.session.has_key('id'):
		ii=request.GET["id"]
		fromform=register_tb.objects.all().filter(id=ii).update(status="rejected")
		return HttpResponseRedirect('/user_approval/')
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def unit_approval(request):
	if request.session.has_key('id'):
		var=unit_register_tb.objects.all().filter(status="pending")
		return render(request,'admin/unit_approval.html',{'db':var})
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def approve_unit(request):
	if request.session.has_key('id'):
		ii=request.GET["id"]
		fromform=unit_register_tb.objects.all().filter(id=ii).update(status="approved")
		return HttpResponseRedirect('/unit_approval/')
	else:
		return render(request,'admin/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def reject_unit(request):
	if request.session.has_key('id'):
		ii=request.GET["id"]
		fromform=unit_register_tb.objects.all().filter(id=ii).update(status="rejected")
		return HttpResponseRedirect('/unit_approval/')
	else:
		return render(request,'admin/login.html')

def admin_waste_reports(request):
    if request.session.get('id') is not None:

        waste_reports = waste_location_tb.objects.all().order_by('-id')

        return render(
            request,
            'admin/waste_reports.html',
            {'db': waste_reports}
        )

    else:
        return render(request, 'admin/login.html')


import json

from django.shortcuts import render, redirect, get_object_or_404

from .models import waste_location_tb
from .gemini_service import identify_waste
from .recycler_matching import find_matching_recyclers



import json
import logging
from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.utils import timezone

from .models import unit_register_tb, waste_location_tb
from .gemini_service import identify_waste
from .recycler_matching import find_matching_recyclers


def admin_waste_image(request):
    if request.session.get('id') is None:
        return render(request, 'admin/login.html')

    waste_id = request.GET.get('id')
    waste = get_object_or_404(waste_location_tb, id=waste_id)

    ai_error = None
    ai_success = None

    if request.method == 'POST':
        action = request.POST.get('action', '')

        # 1. Save waste quantity
        if action == 'save_quantity':
            try:
                quantity = Decimal(
                    request.POST.get('waste_quantity_kg', '').strip()
                )

                if not quantity.is_finite() or quantity <= 0:
                    raise ValueError(
                        'Waste quantity must be greater than zero.'
                    )

                if waste.assigned_recycler_id:
                    if waste.status != 'rejected':
                        raise ValueError(
                            'Quantity cannot be changed while the report '
                            'is assigned or accepted.'
                        )

                waste.waste_quantity_kg = quantity
                waste.save(update_fields=['waste_quantity_kg'])

                return redirect(f'/admin_waste_image/?id={waste.id}')

            except (InvalidOperation, ValueError) as exc:
                ai_error = str(exc) or 'Enter a valid quantity.'

        # 2. Assign or reassign recycler
        elif action == 'assign_recycler':
            recycler_id = request.POST.get('recycler_id', '').strip()

            try:
                with transaction.atomic():
                    # Lock the waste report first.
                    waste = waste_location_tb.objects.select_for_update().get(
                        id=waste.id
                    )

                    # A rejected report may be reassigned.
                    # Other already assigned reports cannot be reassigned.
                    if (
                        waste.assigned_recycler_id
                        and waste.status != 'rejected'
                    ):
                        raise ValueError(
                            'Only an unassigned or rejected report '
                            'can be assigned.'
                        )

                    if (
                        waste.waste_quantity_kg is None
                        or waste.waste_quantity_kg <= 0
                    ):
                        raise ValueError(
                            'Save a valid waste quantity first.'
                        )

                    recycler = get_object_or_404(
                        unit_register_tb.objects.select_for_update(),
                        id=recycler_id,
                        status='approved',
                        is_available=True,
                    )

                    # Calculate capacity already occupied by active reports.
                    active_reports = waste_location_tb.objects.filter(
                        assigned_recycler=recycler
                    ).exclude(
                        status__in=['cancelled', 'rejected']
                    ).exclude(
                        id=waste.id
                    )

                    used_capacity = sum(
                        (
                            report.waste_quantity_kg or Decimal('0')
                            for report in active_reports
                        ),
                        Decimal('0')
                    )

                    capacity = Decimal(
                        str(recycler.available_capacity_kg)
                    )
                    remaining_capacity = capacity - used_capacity

                    if remaining_capacity < waste.waste_quantity_kg:
                        raise ValueError(
                            'This recycler does not have enough '
                            'remaining capacity.'
                        )

                    report_district = (
                        waste.district or ''
                    ).strip().lower()

                    recycler_district = (
                        recycler.district or recycler.place or ''
                    ).strip().lower()

                    if (
                        not report_district
                        or report_district != recycler_district
                    ):
                        raise ValueError(
                            'The selected recycler must belong '
                            'to the same district.'
                        )

                    # Revalidate the current AI matching result.
                    matches = find_matching_recyclers(waste)

                    if not any(
                        match['recycler'].pk == recycler.pk
                        for match in matches
                    ):
                        raise ValueError(
                            'The selected recycler does not match '
                            'the waste type, availability, district, '
                            'or capacity.'
                        )

                    # Replace the old recycler if this is a reassignment.
                    waste.assigned_recycler = recycler
                    waste.assigned_at = timezone.now()
                    waste.status = 'assigned'

                    waste.save(
                        update_fields=[
                            'assigned_recycler',
                            'assigned_at',
                            'status',
                        ]
                    )

                return redirect(f'/admin_waste_image/?id={waste.id}')

            except ValueError as exc:
                ai_error = str(exc)

        # 3. Upload image and analyze using Gemini
        elif action in ('', 'analyze_image'):
            image = request.FILES.get('waste_image')

            if not image:
                ai_error = 'Please select a waste image.'

            elif (
                not image.content_type
                or not image.content_type.startswith('image/')
            ):
                ai_error = 'Please upload a valid image file.'

            elif waste.assigned_recycler_id:
                if waste.status != 'rejected':
                    ai_error = (
                        'The image cannot be changed while the report '
                        'is assigned or accepted.'
                    )
                else:
                    ai_error = (
                        'Unassign the rejected report before changing '
                        'its image.'
                    )

            else:
                try:
                    waste.waste_image = image
                    waste.save(update_fields=['waste_image'])

                    ai_data = identify_waste(waste.waste_image)

                    waste.ai_waste_type = ai_data.get('waste_type', '')
                    waste.ai_material = ai_data.get('material', '')
                    waste.ai_confidence = ai_data.get('confidence')
                    waste.ai_recyclable = ai_data.get('recyclable')
                    waste.ai_result = ai_data.get('result', '')

                    waste.save(
                        update_fields=[
                            'ai_waste_type',
                            'ai_material',
                            'ai_confidence',
                            'ai_recyclable',
                            'ai_result',
                        ]
                    )

                    return redirect(f'/admin_waste_image/?id={waste.id}')

                except Exception:
                    logging.getLogger(__name__).exception(
                        'Gemini analysis failed for waste report %s',
                        waste.id
                    )
                    ai_error = (
                        'Image upload or AI analysis failed. '
                        'Check the server logs.'
                    )

    # 4. Parse saved Gemini results
    ai_items = []
    ai_summary = ''

    if waste.ai_result:
        try:
            saved_result = json.loads(waste.ai_result)

            if isinstance(saved_result, dict):
                items = saved_result.get('items', [])

                if isinstance(items, list):
                    ai_items = [
                        item for item in items
                        if isinstance(item, dict)
                    ]

                ai_summary = saved_result.get('summary', '')
            else:
                ai_summary = str(waste.ai_result)

        except (json.JSONDecodeError, TypeError):
            ai_summary = waste.ai_result

    # 5. Find eligible recyclers
    matched_recyclers = find_matching_recyclers(waste)

    context = {
        'waste': waste,
        'ai_items': ai_items,
        'ai_summary': ai_summary,
        'ai_error': ai_error,
        'ai_success': ai_success,
        'matched_recyclers': matched_recyclers,
    }

    return render(
        request,
        'admin/waste_image.html',
        context
    )



#-----------------------------recycling unit functions-----------------------
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def remove_staff(request):
	if request.session.has_key('id'):
		ii=request.GET["id"]
		fromform=register_tb.objects.all().filter(id=ii).delete()
		return HttpResponseRedirect('/view_workers/')
	else:
		return render(request,'admin/login.html')

import json
from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect
from .models import unit_register_tb


def unit_registration(request):
    if request.method != "POST":
        return render(request, "user/unit_register.html")

    name = request.POST.get("Uname", "").strip()
    email = request.POST.get("email", "").strip().lower()
    password = request.POST.get("psw", "")
    confirm_password = request.POST.get("cnfpsw", "")
    address = request.POST.get("adss", "").strip()
    district = request.POST.get("place", "").strip()
    mobile = request.POST.get("pno", "").strip()
    capacity = request.POST.get("capa", "").strip()
    licence_number = request.POST.get("Lno", "").strip()

    accepted_waste_types = request.POST.getlist(
        "accepted_waste_types"
    )

    is_available = (
        request.POST.get("is_available") == "true"
    )

    # Validate required fields
    if not all([
        name, email, password, confirm_password,
        address, district, mobile, capacity, licence_number
    ]):
        return render(request, "user/unit_register.html", {
            "error": "Please fill in all required fields."
        })

    if password != confirm_password:
        return render(request, "user/unit_register.html", {
            "error": "Passwords do not match."
        })

    if not accepted_waste_types:
        return render(request, "user/unit_register.html", {
            "error": "Please select at least one waste type."
        })

    # Validate numeric capacity
    try:
        available_capacity = Decimal(
            request.POST.get("available_capacity_kg", "")
        )

        if not available_capacity.is_finite() or available_capacity < 0:
            raise InvalidOperation

    except (InvalidOperation, ValueError, TypeError):
        return render(request, "user/unit_register.html", {
            "error": "Please enter a valid available capacity."
        })

    # Check duplicate email
    if unit_register_tb.objects.filter(email=email).exists():
        return render(request, "user/unit_register.html", {
            "error": "Email already registered."
        })

    # Save recycler details
    unit_register_tb.objects.create(
        unit_name=name,
        email=email,
        password=password,
        address=address,
        place=district,
        district=district,
        capacity=capacity,
        mobile_Number=mobile,
        licence_number=licence_number,
        status="pending",
        accepted_waste_types=accepted_waste_types,
        available_capacity_kg=available_capacity,
        is_available=is_available,
    )

    return render(request, "user/home.html", {
        "success": (
            "Registration successful! "
            "Your recycler account is awaiting admin approval."
        )
    })

def recyclingunit_login(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["psw"]
		# print(password)
		chk=unit_register_tb.objects.filter(email=email,password=password,status="approved")
		# print(chk)
		if chk:
			for x in chk:
				request.session['id']=x.id
			return render(request,'recycling_unit/index.html')
		else:
			return render(request,'user/unit_login.html',{'error':'your request is not accepted'})
	else:
		return render(request,'user/unit_login.html')





from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def recyclingunit_profile(request):
    if not request.session.get('id'):
        return render(request, 'user/unit_login.html')

    unit_id = request.session.get('id')

    try:
        recycler = unit_register_tb.objects.get(id=unit_id)
    except unit_register_tb.DoesNotExist:
        request.session.flush()
        return render(request, 'user/unit_login.html')

    if request.method == 'POST':
        unit_name = request.POST.get('unit_name', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        place = request.POST.get('place', '').strip()
        district = request.POST.get('district', '').strip()
        mobile = request.POST.get('mobile_Number', '').strip()
        licence = request.POST.get('licence_number', '').strip()
        waste_types = request.POST.getlist('accepted_waste_types')
        capacity_value = request.POST.get(
            'available_capacity_kg', ''
        ).strip()
        is_available = request.POST.get('is_available') == 'true'

        if not all([unit_name, email, address, place, district, mobile]):
            messages.error(request, 'Please fill all required fields.')
        elif len(unit_name) > 30 or len(email) > 50:
            messages.error(request, 'Unit name or email is too long.')
        elif len(address) > 30 or len(place) > 30:
            messages.error(request, 'Address or place is too long.')
        elif len(district) > 50 or len(mobile) > 30:
            messages.error(request, 'District or mobile number is too long.')
        elif len(licence) > 30:
            messages.error(request, 'Licence number is too long.')
        elif unit_register_tb.objects.filter(
            email=email
        ).exclude(id=unit_id).exists():
            messages.error(request, 'This email is already registered.')
        else:
            try:
                capacity = Decimal(capacity_value)

                if not capacity.is_finite() or capacity < 0:
                    raise ValueError

                # Do not reduce capacity below existing active assignments.
                active_reports = waste_location_tb.objects.filter(
                    assigned_recycler_id=unit_id
                ).exclude(status__in=['rejected', 'cancelled'])

                used_capacity = sum(
                    (
                        report.waste_quantity_kg or Decimal('0')
                        for report in active_reports
                    ),
                    Decimal('0')
                )

                if capacity < used_capacity:
                    messages.error(
                        request,
                        f'Capacity cannot be below the {used_capacity} kg '
                        'currently assigned to you.'
                    )
                else:
                    recycler.unit_name = unit_name
                    recycler.email = email
                    recycler.address = address
                    recycler.place = place
                    recycler.district = district
                    recycler.mobile_Number = mobile
                    recycler.licence_number = licence
                    recycler.accepted_waste_types = waste_types
                    recycler.available_capacity_kg = capacity
                    recycler.is_available = is_available

                    recycler.save()
                    messages.success(request, 'Profile updated successfully!')
                    return redirect('recyclingunit_profile')

            except (InvalidOperation, ValueError):
                messages.error(
                    request,
                    'Enter a valid non-negative capacity.'
                )

    return render(
        request,
        'recycling_unit/profile.html',
        {
            'recycler': recycler,
            'waste_type_options': [
                'Plastic', 'Paper', 'Glass', 'Metal',
                'Electronic Waste', 'Organic Waste'
            ],
        }
    )




from django.shortcuts import render
from .models import waste_location_tb, unit_register_tb


def recyclingunit_home(request):
    if request.session.get('id'):
        unit_id = request.session.get('id')

        # Logged-in recycler details
        recycler = unit_register_tb.objects.filter(
            id=unit_id
        ).first()

        if not recycler:
            return render(request, 'user/unit_login.html')

        # Only reports assigned to this recycler
        assigned_reports = waste_location_tb.objects.filter(
            assigned_recycler_id=unit_id
        ).select_related('user_id').order_by('-assigned_at')

        context = {
            'unit_id': unit_id,
            'recycler': recycler,
            'assigned_reports': assigned_reports,
            'total_reports': assigned_reports.count(),
        }

        return render(
            request,
            'recycling_unit/index.html',
            context
        )

    return render(request, 'user/unit_login.html')



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def view_workers(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		var=workers_register_tb.objects.all().filter(unit_id=ii,workers_type="delivery dept")
		var1=workers_register_tb.objects.all().filter(unit_id=ii,workers_type="collecting dept")

		return render(request,'recycling_unit/workers.html',{'var':var,'var1':var1})
	else:
		return render(request,'user/unit_login.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_products(request):
	if request.session.has_key('id'):
		if request.method=="POST":
			ii=request.session['id']
			uid=unit_register_tb.objects.all().get(id=ii)
			name=request.POST["pname"]
			code=request.POST["pcode"]

			discription=request.POST["pdiscription"]
			stock=request.POST["pstock"]
			price=request.POST["price"]
			pic=request.FILES["img"]

			chk=product_tb.objects.all().filter(code=code)
			if chk:
				return render(request,'recycling_unit/add_product.html',{'error':'Code Already exists'})
			else:
				a=product_tb(unitid=uid,name=name,code=code,description=discription,quantity=stock,price=price,image=pic)
				a.save()
				return HttpResponseRedirect('/products/')

				# return render(request,'recycling_unit/add_product.html')
		else:
			return render(request,'recycling_unit/add_product.html')
	else:
		return render(request,'user/unit_login.html')
	
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_workers(request):
	if request.session.has_key('id'):
		if request.method=="POST":
			ii=request.session['id']
			uid=unit_register_tb.objects.all().get(id=ii)
			name=request.POST["name"]
			email=request.POST["email"]
			password=request.POST["psw"]
			dob=request.POST["dob"]
			address=request.POST["address"]
			mobile=request.POST["pno"]
			place=request.POST["place"]
			w_type=request.POST["wtype"]
			aadhar=request.POST["adr"]


			chk=workers_register_tb.objects.all().filter(email=email,password=password)
			if chk:
				return render(request,'recycling_unit/add_workers.html',{'error':'Email Already exists'})
			else:
				a=workers_register_tb(unit_id=uid,Aadhar_Number=aadhar,name=name,email=email,password=password,dob=dob,address=address,mobile_Number=mobile,place=place,workers_type=w_type)
				a.save()
				return render(request,'recycling_unit/add_workers.html')
		else:
			return render(request,'recycling_unit/add_workers.html')
	else:
		return render(request,'user/unit_login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def products(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		var=product_tb.objects.all().filter(unitid=ii)
		return render(request,'recycling_unit/product.html',{'db':var})
	else:
		return render(request,'user/unit_login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def view_waste_location(request):
    if request.session.get('id'):
        unit_id = request.session.get('id')

        reports = waste_location_tb.objects.filter(
            assigned_recycler_id=unit_id
        ).order_by('-assigned_at')

        return render(
            request,
            'recycling_unit/view_waste_loc.html',
            {'db': reports}
        )

    return render(request, 'user/unit_login.html')

	

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST


@require_POST
def accept_waste(request, waste_id):
    if not request.session.get('id'):
        return redirect('unit_login')

    unit_id = request.session.get('id')

    waste = get_object_or_404(
        waste_location_tb,
        id=waste_id,
        assigned_recycler_id=unit_id
    )

    if waste.status == 'assigned':
        waste.status = 'accepted'
        waste.save(update_fields=['status'])

    return redirect('view_waste_location')


@require_POST
def reject_waste(request, waste_id):
    if not request.session.get('id'):
        return redirect('unit_login')

    unit_id = request.session.get('id')

    waste = get_object_or_404(
        waste_location_tb,
        id=waste_id,
        assigned_recycler_id=unit_id
    )

    if waste.status == 'assigned':
        waste.status = 'rejected'
        waste.save(update_fields=['status'])

    return redirect('view_waste_location')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def allocate_work(request):
	if request.session.has_key('id'):
		if request.method=='POST':
			widd=request.POST["wid"]
			worker=request.POST["worker"]
			var=waste_location_tb.objects.all().filter(id=widd).update(worker_email=worker,status="accepted")
			return HttpResponseRedirect('/view_waste_location/')
		else:
			vv=request.GET['id']
			ii=request.session['id']
			var1=unit_register_tb.objects.all().filter(id=ii)
			for x in var1:
				plc=x.place
			var2=workers_register_tb.objects.all().filter(unit_id=ii,workers_type="collecting dept")
			return render(request,'recycling_unit/allocate_waste_collection.html',{'ob':var2,'wid':vv})
	else:
		return render(request,'user/unit_login.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def view_orders(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		print("_________###########_____________",ii)

		var1=order_item_tb.objects.all().filter(unit_id=ii,status="pending")
		arr=[]
		arr.append(var1)
		print("__________",arr)
		# for x in var1:
		# 	plc=x.place
		# var=waste_location_tb.objects.all().filter(district=plc,status="pending")
		return render(request,'recycling_unit/view_order.html',{'db':var1})
	else:
		return render(request,'user/unit_login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def allocate_order_works(request):
	if request.session.has_key('id'):
		if request.method=='POST':
			print("__________inside post____________")
			widd=request.POST["wid"]
			worker=request.POST["worker"]
			var=order_item_tb.objects.all().filter(id=widd).update(worker_email=worker,status="accepted")
			return HttpResponseRedirect('/view_orders/')
		else:
			vv=request.GET['id']
			ii=request.session['id']
			var1=unit_register_tb.objects.all().filter(id=ii)
			for x in var1:
				plc=x.place
			var2=workers_register_tb.objects.all().filter(unit_id=ii,workers_type="delivery dept")
			return render(request,'recycling_unit/allocate_order_work.html',{'ob':var2,'wid':vv})
	else:
		return render(request,'user/unit_login.html')


#-----------------workers functions--------------------------
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def workers_home(request):
	if request.session.has_key('id'):
		return render(request,'worker/index.html')
	
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def workers_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        chk = workers_register_tb.objects.filter(email=email, password=password)
        if chk.exists():
            for x in chk:
                request.session['id'] = x.id
                return render(request, 'worker/index.html')
        else:
            # Invalid login - send back with error message or stay on login page
            return render(request, 'worker/login.html', {'msg': 'Invalid Email or Password'})
    
    # GET request or any non-POST
    return render(request, 'worker/login.html')

		

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def view_alloted_work(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		print("___________________________",ii)
		var=workers_register_tb.objects.all().filter(id=ii,workers_type="delivery dept")
		print("_______________",var)
		if var:
			for x in var:
				email=x.email
			print("____",email)
			aa=order_item_tb.objects.all().filter(worker_email=email,status="accepted")
			return render(request,'worker/view_alloted_works.html',{'db':aa})
		else:
			var1=workers_register_tb.objects.all().filter(id=ii,workers_type="collecting dept")
			print("___________inside else______")
			for x in var1:
				email=x.email
			bb=waste_location_tb.objects.all().filter(worker_email=email,status="accepted")
			return render(request,'worker/view_alloted_loc_works.html',{'db':bb})
	else:
		return render(request,'worker/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def accepte_work(request):
	if request.session.has_key('id'):
		ii=request.GET['id']
		bb=waste_location_tb.objects.all().filter(id=ii).update(status="proccesing")
		return HttpResponseRedirect('/view_alloted_work/')
	else:
		return render(request,'worker/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def view_accepted_work(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		print("___________________________",ii)
		var=workers_register_tb.objects.all().filter(id=ii,workers_type="delivery dept")
		print("_______________",var)
		if var:
			for x in var:
				email=x.email
			print("____",email)
			aa=order_item_tb.objects.all().filter(worker_email=email,status="proccesing")
			return render(request,'worker/view_accepted_works.html',{'db':aa})
		else:
			var1=workers_register_tb.objects.all().filter(id=ii,workers_type="collecting dept")
			print("___________inside else______")
			for x in var1:
				email=x.email
			bb=waste_location_tb.objects.all().filter(worker_email=email,status="proccesing")
			return render(request,'worker/view_accepted_loc_works.html',{'db':bb})
	else:
			return render(request,'worker/login.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def accepte_order_work(request):
	if request.session.has_key('id'):
		ii=request.GET['id']
		bb=order_item_tb.objects.all().filter(id=ii).update(status="proccesing")
		return HttpResponseRedirect('/view_alloted_work/')
	else:
		return render(request,'worker/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def proccesing_order_work(request):
	if request.session.has_key('id'):
		ii=request.GET['id']
		bb=order_item_tb.objects.all().filter(id=ii).update(status="delivered")
		return HttpResponseRedirect('/view_accepted_work/')
	else:
		return render(request,'worker/login.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def proccesing_work(request):
	if request.session.has_key('id'):
		ii=request.GET['id']
		bb=waste_location_tb.objects.all().filter(id=ii).update(status="collected")
		return HttpResponseRedirect('/view_accepted_work/')
	else:
		return render(request,'worker/login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def finished_works(request):
	if request.session.has_key('id'):
		ii=request.session['id']
		print("___________________________",ii)
		var=workers_register_tb.objects.all().filter(id=ii,workers_type="delivery dept")
		print("_______________",var)
		if var:
			for x in var:
				email=x.email
			print("____",email)
			aa=order_item_tb.objects.all().filter(worker_email=email,status="delivered")
			return render(request,'worker/view_finished_works.html',{'db':aa})
		else:
			var1=workers_register_tb.objects.all().filter(id=ii,workers_type="collecting dept")
			print("___________inside else______")
			for x in var1:
				email=x.email
			bb=waste_location_tb.objects.all().filter(worker_email=email,status="collected")
			return render(request,'worker/view_finished_loc_works.html',{'db':bb})
	else:
		return render(request,'worker/login.html')

def logout(request):
    del request.session['id']
    return HttpResponseRedirect('/')
	
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import feedback_tb  # Import your model

# def view_feedback(request, unit_id):  # Accept unit_id as a parameter
#     feedbacks = feedback_tb.objects.filter(unit_id=unit_id)  # Fetch feedback for the unit
#     return render(request, 'recycling_unit/view_feedback.html', {'feedbacks': feedbacks})

def view_feedback(request):
    if request.session.has_key('id'):
        unit_id = request.session.get('id')  # Fetch logged-in unit's ID
        print(unit_id)  # Debugging purpose

        feedbacks = feedback_tb.objects.filter(unit_id=unit_id)
        print(feedbacks)  # Corrected indentation

        return render(request, 'recycling_unit/view_feedback.html', {'feedbacks': feedbacks, 'unit_id': unit_id})
    else:
        return render(request, 'user/unit_login.html', {'error': 'Please log in first'})
