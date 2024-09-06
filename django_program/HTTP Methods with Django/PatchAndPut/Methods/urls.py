from django.urls import include,path
from .views import *

urlpatterns = [
    path('',view_req,name='viewreq'),
    path('student/',view_Student,name='student')
]
