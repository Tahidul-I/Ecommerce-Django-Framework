from django.urls import path
from frontend import views
urlpatterns = [
    path('',views.home_page, name='home_page'),
    path('category_pro_show<int:id>/',views.category_pro_show, name='category_pro_show'),
    path('pro_details<int:id>/',views.pro_details, name='pro_details'),
    path('search_items/',views.search_items, name='search_items'),
    path('shop/',views.shop, name='shop'),
    

]