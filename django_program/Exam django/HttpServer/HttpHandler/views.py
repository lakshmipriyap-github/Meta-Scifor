from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def Book_View(request):
    dic_books = {
        'books' : Book.objects.all()
    }
    return render(request,'book_list.html',dic_books)

def Add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request,'book_form.html',{'form':form})

def Update_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form})


def Delete_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'book_confirmation.html', {'book': book})
