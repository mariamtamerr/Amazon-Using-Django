from django.urls import path 
from categories import views


urlpatterns = [
    path('', views.home , name='categories index home'),
    path('details/<int:id>', views.details , name='categories details'),
 
]
