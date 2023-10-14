from django.db import models
from django.shortcuts import  reverse
# from pages.models import Product

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # product = models.ForeignKey(Product)
   



    def __str__(self):
        return self.name
    

    @classmethod
    def get_all_categories(cls):
        return  cls.objects.all()


    # @classmethod
    # def get_home_url(cls):
    #     return reverse('home')


    def get_image_url(self):
        return f"/media/{self.image}"
