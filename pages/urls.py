from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us', views.contact_us, name='contact-us'),
    path('about_us', views.about_us, name='about-us'),
    path('home_details/<int:product_id>', views.home_details, name='home_details'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('forms/create', views.createViaForm, name='create'),
 
]
