from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, QuizAttempt, Question,Answer
from .forms import QuizForm
from django.contrib.auth.views import LoginView
from django.urls import reverse



@login_required
def create_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        question_text = request.POST.get('question')
        correct_answer_text = request.POST.get('correct_answer')
        answer_texts = request.POST.getlist('answers')

        if question_text and answer_texts:
            question = Question.objects.create(quiz=quiz, text=question_text)

            # Create answer choices
            for i, answer_text in enumerate(answer_texts):
                is_correct = (answer_text == correct_answer_text)  # Determine if it's the correct answer
                Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

            return redirect("create_question", quiz_id=quiz.id)

    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'create_question.html', context=context)

@login_required
def admin_quiz_list(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes': quizzes,
    }
    return render(request, 'admin_quiz_list.html', context=context)


@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            if title:
                Quiz.objects.create(title=title)
                return redirect('admin_quiz_list')
    else:
        form = QuizForm()
        context = {
            'form' : form,
        }
    return render(request, 'admin_create_quiz.html',context=context)

@login_required
def delete_quiz(request,pk=None):
    Quiz.objects.get(id=pk).delete()
    return redirect('admin_quiz_list')