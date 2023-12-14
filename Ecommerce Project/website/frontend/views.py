# --------------------------------------------------------------------------------------
#                      This App View Is For Handling Frontend
# --------------------------------------------------------------------------------------
from django.shortcuts import render,redirect
from backend.models import*
from django.db.models import Q
from App_order.models import cart
from django.db.models import Prefetch

# Create your views here.
def base_function(request):
    pro_data = product_details.objects.all().prefetch_related('product')
    pro_cat = product_category.objects.all()
    checkout_products = cart.objects.filter( buyer = request.user).all().count()
    

    context = {
        'pro_data':pro_data,
        'pro_cat' : pro_cat,
        'checkout_products':checkout_products,
        
    }

    return render(request,'frontend/base.html',context)




def home_page(request):
    pro_data = product_details.objects.all().prefetch_related('product')
    pro_cat = product_category.objects.all()
    checkout_products = cart.objects.filter( buyer = request.user).all().count()
    carousel_data = product_details.objects.filter(carousel_status = True)

    

    context = {
        'pro_data':pro_data,
        'pro_cat' : pro_cat,
        'checkout_products':checkout_products,
        'carousel_data':carousel_data
        
    }

    return render(request,'frontend/index.html',context)


def category_pro_show(request,id):
    data = product_images.objects.filter(product_id = id).all()
    pro_cat = product_category.objects.all()
    checkout_products = cart.objects.filter( buyer = request.user).all().count()

    context={
        'data':data,
        'pro_cat':pro_cat,
        'checkout_products':checkout_products
    }

    return render(request,'frontend/shop.html',context)

def pro_details(request,id):
    data = id
    pro_cat = product_category.objects.all()
    checkout_products = cart.objects.filter( buyer = request.user).all().count()
    product_img = product_images.objects.get(id = data)
    product_extra = product_images.objects.filter(product_id =product_img.product_id ).all().exclude(id = product_img.id)
    

    context = {
        'product_img':product_img,
        'product_extra':product_extra,
        'checkout_products':checkout_products,
        'pro_cat' : pro_cat,
       
    }

    return render(request,'frontend/detail.html',context)

def search_items(request):
    if request.method=='GET':
        key_info = request.GET.get('q')

        data = product_details.objects.filter( Q(product_caption__icontains=key_info) | Q(old_price__icontains=key_info) | Q(new_price__icontains=key_info) ).prefetch_related('product')
        context={
            'data':data,
        }


    return render(request,'frontend/search.html',context)

def shop(request):
    pro_data = product_details.objects.all().prefetch_related('product')
    pro_cat = product_category.objects.all()
    checkout_products = cart.objects.filter( buyer = request.user).all().count()
    

    context = {
        'pro_data':pro_data,
        'pro_cat' : pro_cat,
        'checkout_products':checkout_products,
        'checkout_products':checkout_products
    }

    return render(request,'frontend/shop_nav.html',context)


