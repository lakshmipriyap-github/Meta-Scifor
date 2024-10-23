from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseForm



# Create your views here.
@login_required
def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses/course_list.html', context=context)

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    context = {
        'form': form,
    }
    return render(request, 'courses/add_course.html', context=context)

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    context = {
        'course': course,
    }
    return render(request, 'courses/course_detail.html', context=context)

@login_required
def delete_course(request,pk=None):
    Course.objects.get(id=pk).delete()
    return redirect('course_list')