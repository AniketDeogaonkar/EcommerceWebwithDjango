from django.db import models

from base.models import BaseModel
# Create your models here.
class Category(BaseModel):
    category_Name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True, blank=True)
    category_Image=models.ImageField(upload_to="categories")
    

class Product(BaseModel):
    product_Name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    slug=models.SlugField(unique=True,null=True, blank=True)
    price=models.IntegerField()
    product_description=models.TextField()



    
class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    image=models.ImageField(upload_to="product")
    