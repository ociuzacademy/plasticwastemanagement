from django.urls import path
from recycling_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

#---------------user url--------------------
	path('',views.index,name='index'),
	path('home/',views.home),
	path('user_login/',views.user_login),
	path('unit_login/',views.recyclingunit_login),
	path('user_registration/',views.user_registration),
	path('unit_registration/',views.unit_registration),
	path('shop/',views.shop),
	path('product_detail_view/',views.product_detail_view),
	path('add_to_cart/',views.add_to_cart),
	path('usercart/',views.cart),
	path('delete_cart/',views.delete_cart),
	path('payment/',views.payment),
	path('user_cart_product_payment/',views.user_cart_product_payment),
	path('product_booking/',views.product_booking),
	path('add_waste_loc/',views.add_waste_location),
	path('profile/',views.profile),
	path('my_order/',views.my_order),
	path('feedback/',views.feedback),
path('view_feedback/', views.view_feedback, name='view_feedback'),




#----------------recycling units url-----------------------


	path('recyclingunit_home/',views.recyclingunit_home),
	path('add_products/',views.add_products),
	path('add_workers/',views.add_workers),
	path('view_waste_location/',views.view_waste_location),
	path('allocate_work/',views.allocate_work),
	path('view_orders/',views.view_orders),
	path('allocate_order_work/',views.allocate_order_works),
	path('products/',views.products),
	path('view_workers/',views.view_workers),
	path('remove_staff/',views.remove_staff),
	
	

#--------------admin urls-----------------------------------

	path('admin_home/',views.admin_home),
	path('admin_login/',views.admin_login),
	path('user_approval/',views.user_approval),
	path('approve_user/',views.approve_user),
	path('reject_user/',views.reject_user),
	path('unit_approval/',views.unit_approval),
	path('approve_unit/',views.approve_unit),
	path('reject_unit/',views.reject_unit),
	path('rejected_user_list/',views.rejected_user_list),
	path('rejected_unit_list/',views.rejected_unit_list),
	path('approved_user_list/',views.approved_user_list),
	path('approved_unit_list/',views.approved_unit_list),



#--------------------workers url----------------

	path('workers_home/',views.workers_home),
	path('workers_login/',views.workers_login),
	path('view_alloted_work/',views.view_alloted_work),
	path('accepte_work/',views.accepte_work),
	path('accepte_order_work/',views.accepte_order_work),
	path('view_accepted_work/',views.view_accepted_work),
	path('proccesing_order_work/',views.proccesing_order_work),
	path('proccesing_work/',views.proccesing_work),
	path('finished_works/',views.finished_works),

	


	



	path('logout/',views.logout),





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)