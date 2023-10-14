from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('home') # NAME NOT PATH .. hna we put NAME of home url not the path to it
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})