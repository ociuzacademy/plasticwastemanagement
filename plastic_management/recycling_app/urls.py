
from django.urls import path
from recycling_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # ---------------- User URLs ----------------
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('unit_login/', views.recyclingunit_login, name='recyclingunit_login'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('unit_registration/', views.unit_registration, name='unit_registration'),
    path('shop/', views.shop, name='shop'),
    path('product_detail_view/', views.product_detail_view, name='product_detail_view'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('usercart/', views.cart, name='cart'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('payment/', views.payment, name='payment'),
    path('user_cart_product_payment/', views.user_cart_product_payment, name='user_cart_product_payment'),
    path('product_booking/', views.product_booking, name='product_booking'),
    path('add_waste_loc/', views.add_waste_location, name='add_waste_location'),
    path('profile/', views.profile, name='profile'),
    path('my_order/', views.my_order, name='my_order'),
    path('feedback/', views.feedback, name='feedback'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),

    # ---------------- Recycling Unit URLs ----------------
    path('recyclingunit_home/', views.recyclingunit_home, name='recyclingunit_home'),
    path('add_products/', views.add_products, name='add_products'),
    path('add_workers/', views.add_workers, name='add_workers'),
    path('view_waste_location/', views.view_waste_location, name='view_waste_location'),
    path('allocate_work/', views.allocate_work, name='allocate_work'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('allocate_order_work/', views.allocate_order_works, name='allocate_order_works'),
    path('products/', views.products, name='products'),
    path('view_workers/', views.view_workers, name='view_workers'),
    path('remove_staff/', views.remove_staff, name='remove_staff'),
    path('recyclingunit_profile/', views.recyclingunit_profile, name='recyclingunit_profile'),
    path('accept_waste/<int:waste_id>/', views.accept_waste, name='accept_waste'),
    path('reject_waste/<int:waste_id>/', views.reject_waste, name='reject_waste'),

    # ---------------- Admin URLs ----------------
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_approval/', views.user_approval, name='user_approval'),
    path('approve_user/', views.approve_user, name='approve_user'),
    path('reject_user/', views.reject_user, name='reject_user'),
    path('unit_approval/', views.unit_approval, name='unit_approval'),
    path('approve_unit/', views.approve_unit, name='approve_unit'),
    path('reject_unit/', views.reject_unit, name='reject_unit'),
    path('rejected_user_list/', views.rejected_user_list, name='rejected_user_list'),
    path('rejected_unit_list/', views.rejected_unit_list, name='rejected_unit_list'),
    path('approved_user_list/', views.approved_user_list, name='approved_user_list'),
    path('approved_unit_list/', views.approved_unit_list, name='approved_unit_list'),
    path('admin_waste_reports/', views.admin_waste_reports, name='admin_waste_reports'),
    path('admin_waste_image/', views.admin_waste_image, name='admin_waste_image'),

    # ---------------- Worker URLs ----------------
    path('workers_home/', views.workers_home, name='workers_home'),
    path('workers_login/', views.workers_login, name='workers_login'),
    path('view_alloted_work/', views.view_alloted_work, name='view_alloted_work'),
    path('accepte_work/', views.accepte_work, name='accepte_work'),
    path('accepte_order_work/', views.accepte_order_work, name='accepte_order_work'),
    path('view_accepted_work/', views.view_accepted_work, name='view_accepted_work'),
    path('proccesing_order_work/', views.proccesing_order_work, name='proccesing_order_work'),
    path('proccesing_work/', views.proccesing_work, name='proccesing_work'),
    path('finished_works/', views.finished_works, name='finished_works'),

    # ---------------- Common URLs ----------------
    path('logout/', views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
