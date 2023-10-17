from django.db import models
from django.shortcuts import reverse
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.


#  {"id": 1, "price": 140, "name": "Half Finger Covers", "image": "1.jpg", "instock": True, "description": "text description"},
   
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=True)
    image = models.ImageField(null=True)
    instock = models.BooleanField()
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='products')
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
 

    @classmethod
    def get_all_products(cls):
        return  cls.objects.all()


    @classmethod
    def get_home_url(cls):
        return reverse('home')


    def get_image_url(self):
        # return f"/media/{self.image}"
        return f"/media/{self.image}"
