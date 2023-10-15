from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pages.models import Product  
from django.views.generic import DetailView
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}. You can now log in')
            return redirect('login') # NAME NOT PATH .. hna we put NAME of home url not the path to it
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


class ProfileDetailView(DetailView):
    model = User # this will come from auth ya zakyya you won't create it !!!
    # template_name = 'users/profile.html'
    # context_object_name = 'user_detail'
    template_name = 'users/profile-detail.html'
    context_object_name = 'profiledetail'


    # KHODY OBJECT MN ELUSER YA ZEKOOOO !
    def get_object(self, queryset=None):
    #  print(self.request.user)
    #  print(user.email)
     return self.request.user

