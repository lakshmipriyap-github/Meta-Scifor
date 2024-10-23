from django.urls import path
from .views import create_question, admin_quiz_list, create_quiz ,delete_quiz
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/quizzes/', admin_quiz_list, name='admin_quiz_list'),
    path('admin/quiz/create/', create_quiz, name='create_quiz'),
    path('admin/quiz/<int:quiz_id>/create_question/', create_question, name='create_question'),
    path('admin/quiz/delete/<int:pk>', delete_quiz, name='delete_quiz'),

]
