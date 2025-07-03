from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from datetime import date
from datetime import datetime

from .models import register_tb,unit_register_tb,waste_location_tb,feedback_tb,workers_register_tb,product_tb,cart_tb,order_tb,order_item_tb
from django.views.decorators.cache import cache_control
# Create your views here.

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

#-----------------------------recycling unit functions-----------------------
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def remove_staff(request):
	if request.session.has_key('id'):
		ii=request.GET["id"]
		fromform=register_tb.objects.all().filter(id=ii).delete()
		return HttpResponseRedirect('/view_workers/')
	else:
		return render(request,'admin/login.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def unit_registration(request):
	if request.method=="POST":
		name=request.POST["Uname"]
		email=request.POST["email"]
		password=request.POST["psw"]
		confimpassword=request.POST["cnfpsw"]
		capacity=request.POST["capa"]
		address=request.POST["adss"]
		mobile=request.POST["pno"]
		place=request.POST["place"]
		lno=request.POST["Lno"]

		chk=unit_register_tb.objects.all().filter(email=email,password=password)
		if chk:
			return render(request,'user/unit_register.html',{'error':'Email Already exists'})
		else:
			a=unit_register_tb(unit_name=name,licence_number=lno,email=email,password=password,capacity=capacity,address=address,mobile_Number=mobile,place=place,status="pending")
			a.save()
			return render(request,'user/home.html',{'success':'successfully registerd'})
	else:
		return render(request,'user/unit_register.html')

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
def recyclingunit_home(request):
    if request.session.has_key('id'):
        unit_id = request.session.get('id')  # Retrieve unit_id from session
        return render(request, 'recycling_unit/index.html', {'unit_id': unit_id})
    else:
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
	if request.session.has_key('id'):
		ii=request.session['id']
		var1=unit_register_tb.objects.all().filter(id=ii)
		for x in var1:
			plc=x.place
		var=waste_location_tb.objects.all().filter(district=plc,status="pending")
		return render(request,'recycling_unit/view_waste_loc.html',{'db':var})
	else:
		return render(request,'user/unit_login.html')
	
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
