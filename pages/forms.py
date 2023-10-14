from django import forms
from pages.models import Product
from categories.models import Category
from django.core.exceptions import ValidationError


class ProductForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(label='Product Name')
    price = forms.IntegerField(required=False)
    image = forms.ImageField(required=False)
    # instock = forms.BooleanField()
    instock = forms.CharField()
    description = forms.CharField(required=False)
    category = forms.ModelChoiceField(Category.get_all_categories(), required=False)

    def clean_name(self):

        # cleaned data
        found = Product.objects.filter(name=self.cleaned_data['name']).exists()
        if found:
            raise ValidationError("This product already exists")
        return self.cleaned_data['name']