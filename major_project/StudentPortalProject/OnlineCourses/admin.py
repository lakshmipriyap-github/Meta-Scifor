from django.contrib import admin
from .models import Course,Enrollment

# Register your models here.
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title','course_id','syllabus')

class EnrollAdmin(admin.ModelAdmin):
    list_display = ('student','course','enrolled_on')

admin.site.register(Course,CoursesAdmin)
admin.site.register(Enrollment,EnrollAdmin)