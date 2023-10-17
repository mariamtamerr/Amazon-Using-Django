
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']




    def clean_username(self):
        username = self.cleaned_data['username']
        if self.instance.username == username:
            return username  
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username Already Exists.")
        
        return username