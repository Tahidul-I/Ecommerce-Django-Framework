from django.urls import path
from App_order import views

urlpatterns = [
    path('cart_add<int:id>',views.cart_add,name='cart_add'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('increament_cart<int:id>/',views.increament_cart,name='increament_cart'),
    path('decreament_cart<int:id>/',views.decreament_cart,name='decreament_cart'),
]