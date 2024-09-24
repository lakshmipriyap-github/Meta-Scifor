# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path  # URL routing
from django.conf import settings  # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/', views.login_page, name='login_page'),  # Login page
    path('logout/', views.logout_view, name='logout_view'),  # Logout page
    path('register/', views.register_page, name='register'),  # Registration page
    path('index/',views.index, name="index"),
    path('delete/<int:id>/', views.delete_item, name="delete"),
]



