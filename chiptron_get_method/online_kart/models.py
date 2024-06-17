from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)

class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
 
  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price
 
class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)

from django.db import models

class Sale(models.Model):
    item_code = models.CharField(max_length=50)
    temp_time = models.DateTimeField()
    temp_value = models.IntegerField()

    def __str__(self):
        return f"{self.item_code} - {self.temp_time}"
    
    
class jove_graph(models.Model):
    company_id=models.CharField(max_length=20)
    location_id=models.CharField(max_length=20)
    battery_group=models.IntegerField()
    battery_id=models.IntegerField()
    voltage=models.IntegerField()
    heat=models.IntegerField()
    current=models.IntegerField()
    bms_data_date=models.DateTimeField()
    bms_system_date=models.DateTimeField()