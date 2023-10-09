from django.db import models

# Create your models here.


#  {"id": 1, "price": 140, "name": "Half Finger Covers", "image": "1.jpg", "instock": True, "description": "text description"},
   
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=True)
    image = models.ImageField(null=True)
    instock = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.name
