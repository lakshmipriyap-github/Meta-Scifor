from django import forms
from .models import QuizAttempt, Quiz, Question


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        choices = [(answer.id, answer.text) for answer in question.answers.all()]
        self.fields['answer'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
