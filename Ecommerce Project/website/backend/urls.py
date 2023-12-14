from django.urls import path
from backend import views,product_details_view
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('user_registration/',views.user_registration, name='user_registration'),
    path('user_login/',views.user_login, name='user_login'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('change_password/',views.change_password, name='change_password'),
    path('practice_registration/',views.practice_registration, name='practice_registration'),
    path('category_product/',product_details_view.category_product, name='category_product'),
    path('product_detail/',product_details_view.product_detail, name='product_detail'),
    path('product_show/',product_details_view.product_show, name='product_show'),
    path('category_info_show/',product_details_view.category_info_show, name='category_info_show'),
    path('product_detail_edit<int:id>/',product_details_view.product_detail_edit, name='product_detail_edit'),
    path('product_delete<int:id>/',product_details_view.product_delete, name='product_delete'),
    path('carousel_data<int:id>/',product_details_view.carousel_data, name='carousel_data'),
]