from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
# -------------------------
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quizattempts')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)  # This should be non-nullable
    total_questions = models.IntegerField(default=0)
    date_attempted = models.DateTimeField(auto_now_add=True)
    is_attempted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('quiz', 'student')
