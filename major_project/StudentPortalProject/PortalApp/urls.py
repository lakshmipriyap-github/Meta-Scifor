from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('admin/home/', views.admin_home, name='admin_home'),

    #notes related url
    path('admin/notes', views.notes, name='notes'),
    path('delete_notes/<int:pk>',views.delete_notes,name='delete_notes'),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name='detail_notes'),

    # Students view all notes created by the admin
    path('notes/', views.students_notes, name='students_notes'),


    # assignment related url
    path('assignment', views.assigments, name='assignment'),
    path('update_assignment/<int:pk>', views.update_assignment, name='update_assignment'),
    path('delete_assignments/<int:pk>', views.delete_assignments, name='delete_assignments'),

    #youtube url
    path('youtube', views.youtube, name='youtube'),

    #todos url
    path('todo', views.todo, name='todo'),
    path('update_todo/<int:pk>', views.update_todo, name='update_todo'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete_todo'),

    # books url
    path('books', views.books, name='books'),

    # quiz urls
    path('quizzes/', views.student_quiz_list, name='student_quiz_list'),
    path('quizzes/<int:quiz_id>/answer/', views.answer_quiz, name='answer_quiz'),

    # course related urls
    path('courses/', views.student_course_list, name='student_course_list'),
    path('courses/<str:course_id>/', views.student_course_detail, name='student_course_detail'),
    path('courses/enroll/<int:course_id>/', views.enroll_in_course, name='enroll_in_course'),

]
