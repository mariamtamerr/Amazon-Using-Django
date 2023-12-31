"""
URL configuration for amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static


# from users import views as user_views
# from django.contrib.auth import views as auth_views

# --------------
# from django.contrib.auth.views import LoginView, LogoutView
# from users.views import ProfileDetailView
# ---------------------

# note : include takes an APP url not a page in an app url
# so it's page.urls for all , not home.urls w contact.urls, ...
#ashan all of them are in the same app

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pages.urls')), 
    # path('api/', include('pages.api.urls')), 
    # path('users/', user_views.profile, name='profile'),
    # path('users/', ProfileDetailView.as_view(), name='profile_detail'),

    path('categories/', include('categories.urls')), 
    # path('register/', user_views.register, name='register'),
    # path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),


    # path('users/', include('users.urls')), 
    path('accounts/', include('accounts.urls')), 
  
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  

# from pages import views  

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'), 
#     path('contact-us/', views.contact_us, name='contact-us'), 
#     path('about-us/', views.about_us, name='about-us'), 
#     # path('/home-details', views.home_details, name='home_details'), 
#     path('home_details/<int:product_id>/', views.home_details, name='home_details'),  # Include this line
# ]

