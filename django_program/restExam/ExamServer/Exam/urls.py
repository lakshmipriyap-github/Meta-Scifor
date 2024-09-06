from django.urls import include,path
from .views import *

urlpatterns = [
    path('',view_req,name='viewreq'),
    path('book/',view_book,name='book')
]
