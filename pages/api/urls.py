

from django.urls import path
from pages.api.views import index, special


urlpatterns = [
    path('', index, name='api index'),
    path('<int:id>', special, name='api special'),
]
