from django.shortcuts import render,redirect,get_object_or_404
from backend.models import product_details,product_images,product_category
from App_order.models import cart, order
import sweetify

# Create your views here.



def cart_add (request, id):
    item = get_object_or_404(product_images, id = id )
    cart_item = cart.objects.get_or_create(item =item, buyer = request.user, purchased = False )
    # purchased=True means payment has been done
    item_order = order.objects.filter( user = request.user, ordered = False)
    # ordered = False means the payment has been done
    # if check_order_obj exist then it means a order is ongoing, so have to add the item 
    # under that order. If if check_order_obj does not exist, we have create a new order

    #1 for addingg or increasing the number of items

    if item_order.exists():
        orders = item_order[0]

        if orders.order_items.filter( item = item, buyer = request.user).exists():
            cart_item[0].quantity += 1
            cart_item[0].save()
            sweetify.success(request,'Item Increamented Successfully')
            return redirect('cart_view')
        else:
            orders.order_items.add(cart_item[0])
            sweetify.success(request,'Item Added Successfully')
            return redirect('cart_view')
        
    else:
        orders = order( user = request.user )
        orders.save()
        orders.order_items.add(cart_item[0])
        sweetify.success(request,'Item Added Successfully')
        return redirect('cart_view' )




def cart_view(request):
    pro_cat = product_category.objects.all()
    carts = cart.objects.filter(buyer = request.user, purchased = False).select_related('item')
    for i in carts:
        print(i)
    orders = order.objects.filter(user = request.user, ordered = False)
    if carts.exists() and orders.exists():
        status =True
        order_item = orders[0]
        context = {
            'carts':carts,
            'order_item':order_item,
            'status':status,
            'pro_cat':pro_cat,
        }
        return render(request, 'App_order/cart_view.html',context)
    
    else:
        status = False
        context = {
            'status':status
        }
        return render(request, 'App_order/cart_view.html',context)

def increament_cart(request,id):
    cart_items = cart.objects.get( id=id, buyer=request.user )
    cart_items.quantity += 1
    cart_items.save()
    return redirect('cart_view')

def decreament_cart(request,id):
    cart_items = cart.objects.get( id=id, buyer=request.user )
    cart_items.quantity -= 1
    if cart_items.quantity == 0:
        cart_items.delete()
        return redirect('cart_view')
    else:
        cart_items.save()
        return redirect('cart_view')

    


    

