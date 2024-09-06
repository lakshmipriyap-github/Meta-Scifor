from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForms

# Create your views here.
def Index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    dic_docs  = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dic_docs)

def booking(request):
    if request.method == 'POST':
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')

    form = BookingForms()
    dict_form = {
        'form' : form
    }
    return render(request,'booking.html',dict_form)

def contact(request):
    return render(request,'contacts.html')

def department(request):
    dic_dept = {
        'dept' : Departments.objects.all()
    }
    return render(request,'department.html',dic_dept)