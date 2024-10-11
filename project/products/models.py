from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name







class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category,related_name='product_category',on_delete=models.SET_NULL,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="product_image")
    def __str__(self):
        return self.name
