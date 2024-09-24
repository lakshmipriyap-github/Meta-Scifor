from django.urls import include,path
from .models import Book
from .views import Add_book,Update_book,Delete_book,Book_View

urlpatterns = [
    path('books/',Book_View,name = 'book_list'),
    path('books/add',Add_book,name = 'add_book'),
    path('books/update/<int:pk>',Update_book,name = 'update_book'),
    path('books/delete/<int:pk>',Delete_book,name = 'delete_book'),
]
