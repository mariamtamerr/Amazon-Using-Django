

# creating API :
from django.urls import path, include
# from django.contrib.auth.models import User
from pages.models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Serializers define the API representation.
class ProductSerializer(serializers.Serializer):
    # id = serializers.IntegerField(primary_key=True)
    id = serializers.IntegerField(label='ID', read_only=True)  
    name = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=Product.objects.all())])
    price = serializers.IntegerField()
    image = serializers.ImageField()
    instock = serializers.BooleanField()
    description = serializers.CharField(allow_null=True, max_length=500)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)




    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.instock = validated_data.get('instock', instance.instock)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance