from django.urls import path
from . import views

urlpatterns = [
    path('youtubedownloader',views.youtube,name="youtube")
]
