from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.contrib.auth.models import  User
from  accounts.forms import UserRegisterForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')





class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None): #Returns the single object that this view will display.
        return self.request.user         #return the currently logged-in user   

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'accounts/profile_update.html'
    fields = ['first_name', 'last_name', 'email']
    # fields = ['firstname', 'lastname', 'username', 'email']
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    def test_func(self):
        return self.request.user == self.get_object()

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('register')

    def get_object(self, queryset=None):
        return self.request.user

    def test_func(self):
        return self.request.user == self.get_object()



class CreateCustomUser(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    # login_url = reverse('login')
    success_url = reverse_lazy("login")