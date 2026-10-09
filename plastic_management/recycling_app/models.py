from django.db import models

# Create your models here.
class register_tb(models.Model):
	name=models.CharField(max_length=30,default='')
	email=models.CharField(max_length=50,default='')
	password=models.CharField(max_length=30,default='')
	gender=models.CharField(max_length=30,default='')
	address=models.CharField(max_length=30,default='')
	place=models.CharField(max_length=30,default='')
	mobile_Number=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='0')
	Aadhar_Number=models.CharField(max_length=30,default='0')



from django.db import models


class unit_register_tb(models.Model):
    unit_name = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=30, default='')
    place = models.CharField(max_length=30, default='')
    capacity = models.CharField(max_length=30, default='')
    mobile_Number = models.CharField(max_length=30, default='')
    status = models.CharField(max_length=30, default='0')
    licence_number = models.CharField(max_length=30, default='0')

    # Recycler matching fields
    district = models.CharField(max_length=50, default='', blank=True)

    accepted_waste_types = models.JSONField(default=list, blank=True)

    available_capacity_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.unit_name



class product_tb(models.Model):
	unitid=models.ForeignKey(unit_register_tb,on_delete=models.CASCADE)
	name=models.CharField(max_length=30,default='')
	code=models.CharField(max_length=30,default='')
	description=models.CharField(max_length=290,default='')
	image=models.ImageField(upload_to = 'files')
	price=models.CharField(max_length=30,default='')
	quantity=models.CharField(max_length=30,default='')

class cart_tb(models.Model):
	user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	product_id=models.ForeignKey(product_tb,on_delete=models.CASCADE)
	unit_id=models.ForeignKey(unit_register_tb,on_delete=models.CASCADE)
	quantity=models.CharField(max_length=30,default='')
	total=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=10,default='0')

class order_tb(models.Model):

	user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	product_id=models.CharField(max_length=30,default='')
	payment=models.CharField(max_length=30,default='')
	date=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
	total=models.CharField(max_length=30,default='')
	payment_status=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')
	cart_id=models.CharField(max_length=30,default='')
	unit_id=models.CharField(max_length=30,default='')




	
class order_item_tb(models.Model):
	order_id=models.ForeignKey(order_tb,on_delete=models.CASCADE)
	user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	product_id=models.ForeignKey(product_tb,on_delete=models.CASCADE)
	unit_id=models.ForeignKey(unit_register_tb,on_delete=models.CASCADE)
	cart_id=models.ForeignKey(cart_tb,on_delete=models.CASCADE)
	total=models.CharField(max_length=30,default='')
	date=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
	payment_status=models.CharField(max_length=30,default='')
	worker_email=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')
	


class workers_register_tb(models.Model):
	unit_id=models.ForeignKey(unit_register_tb,on_delete=models.CASCADE)
	name=models.CharField(max_length=30,default='')
	email=models.CharField(max_length=50,default='')
	password=models.CharField(max_length=30,default='')
	dob=models.CharField(max_length=30,default='')
	address=models.CharField(max_length=30,default='')
	place=models.CharField(max_length=30,default='')
	mobile_Number=models.CharField(max_length=30,default='')
	workers_type=models.CharField(max_length=30,default='0')
	Aadhar_Number=models.CharField(max_length=30,default='0')


class waste_location_tb(models.Model):
	user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	subject=models.CharField(max_length=30,default='')
	description=models.CharField(max_length=100,default='')
	address=models.CharField(max_length=30,default='')
	place=models.CharField(max_length=100,default='')
	district=models.CharField(max_length=30,default='')
	worker_email=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')
	waste_image = models.ImageField(upload_to='waste_images/',null=True,blank=True)
	ai_waste_type = models.CharField(max_length=100,null=True,blank=True)
	ai_material = models.CharField(max_length=100,null=True,blank=True)
	ai_confidence = models.FloatField(null=True,blank=True)
	ai_recyclable = models.BooleanField(null=True,blank=True)
	ai_result = models.TextField(null=True,blank=True)
	waste_quantity_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
	    # Recycler assignment
	assigned_recycler = models.ForeignKey(
        unit_register_tb,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_waste_reports'
    )

	assigned_at = models.DateTimeField(
        null=True,
        blank=True
    )

class feedback_tb(models.Model):
	user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
	product_id=models.ForeignKey(product_tb,on_delete=models.CASCADE)
	unit_id=models.ForeignKey(unit_register_tb,on_delete=models.CASCADE)
	feedback=models.CharField(max_length=30,default='')