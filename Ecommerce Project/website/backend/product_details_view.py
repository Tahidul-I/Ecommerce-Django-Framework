# --------------------------------------------------------------------------------------
#              This App View Handles Backend Dashboard Product Related  View
# --------------------------------------------------------------------------------------

from django.shortcuts import render,redirect
from backend.models import*
# --------------------------------------------------------------------------------------
#                          Categorywise   Product   view  starts
# --------------------------------------------------------------------------------------
def category_product(request):

    if request.method=='POST' and request.FILES:
        catagory = request.POST.get('category_name')
        feature_image = request.FILES['feature_image']
        user_save = product_category(
            catagory = catagory,
            category_image = feature_image
        )
        user_save.save()
        return redirect('category_info_show')


    return render(request,'backend/product_details/category.html')

def product_detail(request):

    category_data = product_category.objects.all()
    # product_images_data = product_images.objects.all()
    context={
        'category_data':category_data,
        # 'product_images_data':product_images_data
    }
    if request.method=='POST' and request.FILES:
        product_caption = request.POST.get('caption')
        cat_name    = request.POST.get('category_name')
        old_price = request.POST.get('old_price')
        new_price = request.POST.get('new_price')
        description = request.POST.get('description')
        prod_fiture_img = request.FILES['fiture_image']
        product_image = request.FILES.getlist('product_image')

        save_data = product_details(
            product_caption = product_caption,
            category_name_id = cat_name,
            old_price = old_price,
            new_price = new_price,
            prod_fiture_ima = prod_fiture_img,
            description = description,
        )
        save_data.save()
        product_id = save_data.id

        for i in product_image:
            product_image = product_images(
                pro_images = i,
                product_id = product_id
            )
            product_image.save()


        # for img in category_image:
        #     save_img = product_images(
        #         pro_images = img
        #     )
        #     save_img.save()
        
        return redirect('product_show')
    return render(request,'backend/product_details/product_details.html',context)


def product_show(request):

    # product_data = product_details.objects.all()
    product_data = product_details.objects.prefetch_related('product')
    context = {
        'product_data':product_data,
    }
    return render(request,'backend/product_details/product_show_info.html',context)

def category_info_show(request):
    category_data = product_category.objects.all()
    context = {
        'category_data':category_data,
    }
    return render(request,'backend/product_details/show_category_info.html',context)


def product_detail_edit(request,id):

    data = product_details.objects.filter(id=id).prefetch_related('product')
    category_data = product_category.objects.all()
    context={
        'data':data,
        'category_data':category_data,
    }


    if request.method=='POST' and request.FILES:
        product_caption = request.POST.get('caption')
        cat_name    = request.POST.get('category_name')
        old_price = request.POST.get('old_price')
        new_price = request.POST.get('new_price')
        description = request.POST.get('description')
        prod_fiture_img = request.FILES['fiture_image']
        product_image = request.FILES.getlist('product_image')

        save_data = product_details.objects.filter(id=id)

        save_data = product_details(
            id = id,
            product_caption = product_caption,
            category_name_id = cat_name,
            old_price = old_price,
            new_price = new_price,
            prod_fiture_ima = prod_fiture_img,
            description = description,
        )
        save_data.save()
        product_id = save_data.id

        for i in product_image:
            product_image = product_images(
                pro_images = i,
                product_id = product_id
            )
            product_image.save()

            return redirect('product_show')
        
    return render(request,'backend/product_details/edit_pro.html',context)


def product_delete(request,id):
    data = product_details.objects.filter(id=id)
    data.delete()
    return redirect('product_show')

# --------------------------------------------------------------------------------------
#                          Categorywise   Product   view  ends
# --------------------------------------------------------------------------------------


def carousel_data(request,id):
    data = product_details.objects.get(id=id)
    context = {
        'data':data
    }
    
    if data.carousel_status == False:
             
        if request.method=='POST' and request.FILES:
        
                
            carousel_caption = request.POST.get('caption')
            disount_percentage = int(request.POST.get('discount'))
            carousel_fiture_ima = request.FILES['carousel_fiture_image']
            original_price = data.new_price*(disount_percentage/100)

            save_data = product_details(
                id =id,
                carousel_caption = carousel_caption,
                new_price = original_price,
                old_price = data.new_price,
                product_caption = data.product_caption,
                description = data.description,
                category_name_id = data.category_name,
                prod_fiture_ima = data.prod_fiture_ima,
                disount_percentage = disount_percentage,
                carousel_fiture_ima = carousel_fiture_ima,
                carousel_status = True

            )
            save_data.save()
            return redirect('product_show')
        return render(request,'backend/product_details/carousel_detail.html',context)

        
    else:
        data.carousel_fiture_ima.delete()
        data.carousel_status = False
        data.save()
        
        return redirect('product_show')
            
    
    




