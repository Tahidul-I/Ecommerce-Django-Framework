from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=True,null=True)
    user_image = models.ImageField(upload_to='user_registration/',blank=True,null=True)


class practice_user(models.Model):
    username = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length=100,blank=True, null=True)
    user_image = models.ImageField(upload_to='practice_user_registration/',blank=True,null=True)

class product_category(models.Model):
    id = models.AutoField(primary_key=True)
    catagory = models.CharField(max_length=100, blank=True,null=True)
    category_image = models.ImageField(upload_to='category_image/',blank=True,null=True)

    # def __str__(self):
    #     return self.catagory

class product_details(models.Model):
    id = models.AutoField(primary_key=True)
    # category_name = models.CharField(max_length=100, blank=True,null=True)
    category_name = models.ForeignKey(product_category,on_delete=models.CASCADE,blank = True,null=True)
    product_caption = models.CharField(max_length=100, blank=True,null=True)
    old_price = models.FloatField(blank=True,null=True)
    new_price = models.FloatField(blank=True,null=True)
    prod_fiture_ima = models.ImageField(upload_to='fiture_image/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    # ----------------------------------------------------------------------------
    #             For Carousel data, the below fields will be used
    # ----------------------------------------------------------------------------
    carousel_fiture_ima = models.ImageField(upload_to='carousel_fiture_image/',blank=True,null=True)
    carousel_status = models.BooleanField(default=False)
    disount_percentage = models.IntegerField(blank=True,null=True)
    carousel_caption = models.CharField(max_length=100, blank=True,null=True)


# class dicounted_carousel(models.Model):
#     id = models.AutoField(primary_key=True)
#     product_name = models.CharField( max_length = 250, blank=True, null=True )
#     dicount = models.FloatField( blank=True, null=True, )
#     description = models.TextField( blank=True, null=True )
#     original_price = models.FloatField( blank= True, null=True)
#     dicounted_price =  models.FloatField( blank= True, null=True )
#     carousel_image = models.ImageField(upload_to='discount_images/',blank=True,null=True)

class product_images(models.Model):
    id = models.AutoField(primary_key=True)
    pro_images = models.ImageField(upload_to='product_images/',blank=True,null=True)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE,related_name='product',blank=True,null=True)
    


# class dicounted_carousel(models.Model):
#     product_name = models.CharField( max_length = 250, blank=True, null=True )
#     dicount = models.FloatField( blank=True, null=True, )
#     description = models.TextField( blank=True, null=True )
#     original_price = models.FloatField( blank= True, null=True)
#     dicounted_price =  models.FloatField( blank= True, null=True )
#     carousel_image = models.ImageField(upload_to='discount_images/',blank=True,null=True)
#     rel_with_pro_img = models.OneToOneField(product_images,on_delete=models.CASCADE,related_name='carousel',blank=True,null=True)
#     rel_with_product = models.OneToOneField(product_details,on_delete=models.CASCADE,related_name='carousel_product',blank=True,null=True)

    


 


