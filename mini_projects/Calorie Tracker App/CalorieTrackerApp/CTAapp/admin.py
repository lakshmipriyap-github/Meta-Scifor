from django.contrib import admin
from .models import Food, Consume

# Register your models here.
class Food_Disp(admin.ModelAdmin):
    list_display = ('name','carbs','protein','fats','calories')

admin.site.register(Food,Food_Disp)


class User_Cons(admin.ModelAdmin):
    list_display = ('user','food_consumed')

admin.site.register(Consume,User_Cons)

