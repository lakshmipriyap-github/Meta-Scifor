from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    Desc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'notes'
        verbose_name_plural = 'notes'

class Assignments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'assignments'
        verbose_name_plural = 'assignments'

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todos'
        verbose_name_plural = 'todos'
