from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#  forms for notes
class NotesForms(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','Desc']

        labels = {
            'title' :   'Notes Title',
            'Desc'  :   'Notes Description'
        }
class DateInput(forms.DateInput):
    input_type = 'date'

# forms for assignment
class AssignmentForms(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ['subject','title','description','due','finished']

        widgets = {
                    'due' : DateInput(),
                }

# forms for youtube and books
class YoutubeForm(forms.Form):
    text = forms.CharField(max_length=200,label="What would you like to watch")

class BookForm(forms.Form):
    text = forms.CharField(max_length=200,label="What would you like to read")

#  forms for todo
class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','finished']

# forms for user registration
class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


# class BookingForms(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = '__all__'
#
#         widgets = {
#             'booking_date' : DateInput(),
#         }
#
#         labels = {
#             'p_name' : 'Patient  Name   ',
#             'p_phone': 'Patient Phone  ',
#             'p_email': 'Patient Email  ',
#             'doc_name': 'Doctor Name  ',
#             'booking_date' :'Booking Date '
#
#         }