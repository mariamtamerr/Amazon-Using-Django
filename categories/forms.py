
from django import forms
from categories.models import Category
from django.core.exceptions import ValidationError


class CategoryForm(forms.Form):
    
    name = forms.CharField(label='Product Name')
    image = forms.ImageField(required=False)
    # instock = forms.BooleanField()
    description = forms.CharField(required=False)

    def clean_name(self):

        # cleaned data
        found = Category.objects.filter(name=self.cleaned_data['name']).exists()
        if found:
            raise ValidationError("This product already exists")
        return self.cleaned_data['name']