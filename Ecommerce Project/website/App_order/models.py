from django.db import models
from backend.models import User,product_details,product_images

# Create your models here.
class cart(models.Model):
    buyer = models.ForeignKey(User, on_delete = models.CASCADE, blank=True,null=True,related_name='cart_user')
    item = models.ForeignKey(product_images, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default = 1)
    purchased = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateField(auto_now= True)

    
    
    def get_total(self):
        total = self.item.product.new_price * self.quantity
        float_total = format(total, '0.2f')
        return float_total 
    
class order(models.Model):
    order_items = models.ManyToManyField(cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    ordered = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add=True)
    payment_ID = models.CharField(max_length= 300, blank=True,null=True)
    order_ID = models.CharField(max_length=200, blank=True,null=True)

    def get_totals(self):
        total = 0
        for i in self.order_items.all():
            total += float(i.get_total())

        return total
    def __str__(self):
        return self.user.username
