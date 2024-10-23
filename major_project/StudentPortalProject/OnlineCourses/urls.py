from django.urls import path
from .views import course_list, add_course, course_detail, delete_course

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('courses/add/', add_course, name='add_course'),
    path('courses/<str:course_id>/', course_detail, name='course_detail'),
    path('courses/delete/<int:pk>', delete_course, name='delete_course'),

]
