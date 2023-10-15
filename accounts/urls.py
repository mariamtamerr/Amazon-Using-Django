

from django.urls import path,include
from .views import ProfileDetailView, ProfileUpdateView, ProfileDeleteView, CreateCustomUser
urlpatterns = [
    
    path('',include('django.contrib.auth.urls')), # ready built in by django 3shan yshof el templates el barra bto3 el registration
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('register/', CreateCustomUser.as_view(), name='register'),
]