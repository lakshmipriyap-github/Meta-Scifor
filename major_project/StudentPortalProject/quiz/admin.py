from django.contrib import admin
from .models import Quiz, QuizAttempt, Question,Answer

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title',)

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date_attempted')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizAttempt, QuizAttemptAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)