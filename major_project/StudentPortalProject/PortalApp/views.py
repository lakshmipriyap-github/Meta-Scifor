from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.views import LoginView
from django.views import generic
from django.views.generic import DetailView


from youtubesearchpython import VideosSearch
import requests
from django.urls import reverse

# from current apps model and forms
from .forms import *
from .models import *

# other app import
from quiz.models import Quiz, Question, QuizAttempt ,Answer
from OnlineCourses.models import Course ,Enrollment

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Your login template

    def get_success_url(self):
             if self.request.user.is_superuser:
                 return reverse('admin_home')  # Redirect to home for admin
             else:
                 return reverse('home')  # Redirect to admin_home for other users

# views for admin page.
@login_required
def admin_home(request):
    context = {
        'user': request.user,
    }
    return render(request, 'admin_home.html')


# view for home page
@login_required
def home(request):
    context = {
        'user': request.user,
    }
    return render(request,"home.html",context=context)

# view for youtube
@login_required
def youtube(request):
    if request.method == 'POST':
        form = YoutubeForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        res_list = []
        for i in video.result()['result']:
            res_dict = {
                'input' : text,
                'title' : i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet'] :
                for j in i['descriptionSnippet'] :
                    desc += j['text']
            res_dict['description'] = desc
            res_list.append(res_dict)
            context = {
                'form': form,
                'results' : res_list
            }
        return render(request, 'youtube.html', context=context)
    else:
        form = YoutubeForm()
    context = {
        'form' : form,
    }
    return render(request,'youtube.html',context=context)

# views for book section
@login_required
def books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        text = request.POST['text']
        url = 'https://www.googleapis.com/books/v1/volumes?q='+text
        req = requests.get(url)
        req_js = req.json()
        res_list = []
        for i in range(10):
            res_dict = {
                'title' : req_js['items'][i]['volumeInfo']['title'],
                'subtitle': req_js['items'][i]['volumeInfo'].get('subtitle'),
                'description': req_js['items'][i]['volumeInfo'].get('description'),
                'count': req_js['items'][i]['volumeInfo'].get('pagCount'),
                'categories': req_js['items'][i]['volumeInfo'].get('categories'),
                'rating': req_js['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail': req_js['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview': req_js['items'][i]['volumeInfo'].get('previewLink'),
            }
            res_list.append(res_dict)
            context = {
                'form': form,
                'results' : res_list
            }
        return render(request, 'books.html', context=context)
    else:
        form = BookForm()
    context = {
        'form' : form,
    }
    return render(request,'books.html',context=context)


# --------------views for "notes" section----------------------
@login_required
@user_passes_test(lambda u: u.is_staff)
def notes(request):
    if request.method == 'POST':
        form = NotesForms(request.POST)
        if form.is_valid():
            note = Notes(user=request.user,title=request.POST['title'],Desc=request.POST['Desc'])
            note.save()
        messages.success(request,f"Notes Added from { request.user.username} Successfully !")
        return redirect("notes")
    else:
        form = NotesForms()
    note = Notes.objects.filter(user=request.user)
    context = {
         'notes' : note,
         'form' : form
    }
    return render(request,"notes.html",context=context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_notes(request,pk=None):
    Notes.objects.get(id = pk).delete()
    messages.success(request, "Note deleted successfully!")
    return redirect("notes")

@login_required
def students_notes(request):
    notes = Notes.objects.all()  # Retrieve all notes, since admins create them
    context = {
         'notes': notes,
    }
    return render(request, "notes.html", context=context)

class NotesDetailView(generic.DetailView):
    model = Notes
    template_name = 'notes_detail.html'

# ---------------notes end here ---------------------------

# ---------------views for assignments sections -----------------
@login_required
def assigments(request):
    if request.method == 'POST':
        form = AssignmentForms(request.POST)
        if form.is_valid():
            finished = request.POST.get('finished') == 'on'
            assign = Assignments(
                user= request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                finished = finished
            )
            assign.save()
            messages.success(request, f"Assignments added from {request.user.username} Successfully !")
            return redirect('assignment')
    else:
        form = AssignmentForms()

    assign = Assignments.objects.filter(user = request.user)
    assign_done = not assign

    context = {
        'assignments' : assign,
        'assign_done' : assign_done,
        'form' : form,
    }
    return render(request,'assignment.html',context=context)


@login_required
def update_assignment(request,pk=None):
    assignment = Assignments.objects.get(id=pk)
    if assignment.finished == True:
        assignment.finished = False
    else:
        assignment.finished = True
    assignment.save()
    return redirect('assignment')

@login_required
def delete_assignments(request,pk=None):
    Assignments.objects.get(id=pk).delete()
    return redirect('assignment')

# -------------- assignments end here--------------

# ---------------- views for todos list---------------
@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid():
            finished = request.POST.get('finished') == 'on'
            todos = Todo(
                user=request.user,
                title=request.POST['title'],
                finished=finished
            )
            todos.save()
            messages.success(request, f"Todo added from {request.user.username} Successfully !")
            return redirect('todo')
    else:
        form = TodoForms()

    todos = Todo.objects.filter(user = request.user)
    todos_done = not todos
    context = {
        'todos' : todos,
        'todos_done' : todos_done,
        'form' : form,
    }
    return render(request,'todo.html',context=context)

@login_required
def update_todo(request,pk=None):
    todos = Todo.objects.get(id=pk)
    if todos.finished == True:
        todos.finished = False
    else:
        todos.finished = True
    todos.save()
    return redirect('todo')

@login_required
def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

# --------------- todos end here --------------------

# Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username} !!!")
            return redirect("login")
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'register.html',context=context)

#  profile
@login_required
def profile(request):
    assign = Assignments.objects.filter(finished=False,user=request.user)
    todos = Todo.objects.filter(finished=False,user=request.user)

    if len(assign) == 0:
        assign_done = True
    else:
        assign_done = False

    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False

    context = {
        'assign' : assign,
        'assign_done' : assign_done,
        'todos' : todos,
        'todos_done' : todos_done,
    }
    return render(request,'profile.html',context=context)

# Quiz for students
@login_required
def student_quiz_list(request):
    quizzes = Quiz.objects.all()
    # attempts = QuizAttempt.objects.filter(student=request.user)
    attempts = {attempt.quiz.id: attempt for attempt in QuizAttempt.objects.filter(student=request.user)}
    context = {
        'quizzes': quizzes,
        'attempts': attempts,
    }

    return render(request, 'student_quiz_list.html', context=context)

@login_required
def answer_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # Try to get or create the attempt
    attempt , created = QuizAttempt.objects.get_or_create(quiz=quiz, student=request.user)

    # If the quiz has already been attempted, redirect or display a message
    if attempt.is_attempted:
        return render(request, 'quiz_locked.html', {'score': attempt.score, 'total_questions': attempt.total_questions})

    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()

        if total_questions == 0:
            attempt.score = 0
            attempt.total_questions = total_questions
            attempt.is_attempted = True
            attempt.save()
            return redirect('student_quiz_list')

        for question in questions:
            user_answer_id = request.POST.get(f'question_{question.id}')  # Get the selected answer ID
            if user_answer_id:
                selected_answer = get_object_or_404(Answer, id=user_answer_id)
                if selected_answer.is_correct:
                    score += 1

        # Save the attempt with the calculated score
        attempt.score = score
        attempt.total_questions = total_questions
        attempt.is_attempted = True  # Mark as attempted
        attempt.save()

        context = {
            'quizzes': quiz,
            'attempts' : attempt,
        }
        return redirect('student_quiz_list')
        # return render(request,'student_quiz_list.html',context=context)

    context = {
        'quiz': quiz,
        'questions': questions,
    }

    return render(request, 'answer_quiz.html', context= context)

# Courses related views
@login_required
def student_course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses/students_course_list.html', context=context)

@login_required
def student_course_detail(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    enrolled = False

    if request.user.is_authenticated:
        enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()

    context = {
        'course': course,
        'enrolled': enrolled,
    }
    return render(request, 'courses/students_course_detail.html', context=context)

@login_required
def enroll_in_course(request, course_id):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, id=course_id)
        Enrollment.objects.get_or_create(student=request.user, course=course)
        messages.success(request, f"Enrolled Successfully !")
        return redirect('student_course_list')  # Redirect to the course list or a success page

    else:
        return redirect('login')