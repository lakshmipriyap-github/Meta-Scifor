from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_id = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(upload_to='course_pictures/')
    syllabus = models.TextField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
