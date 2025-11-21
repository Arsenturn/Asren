from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_image = models.ImageField(upload_to='cat_images/')

    def __str__(self):
        return f'Категоринин аты: {self.category_name} '

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_photo', null=True, blank=True )
    phone_number = PhoneNumberField()
    product_type = models.BooleanField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name