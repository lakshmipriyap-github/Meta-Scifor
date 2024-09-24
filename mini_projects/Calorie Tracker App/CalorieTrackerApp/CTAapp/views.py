# Import necessary modules and models
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
import requests
import json

# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        query = request.POST['query']
        api_url = "https://api.api-ninjas.com/v1/nutrition?query="
        api_request = requests.get(api_url + query ,headers={'X-Api-Key': 'SAup/N7apD8HrY60+ErtNg==hPcddn7rgZKQRiiG'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There is an error"
            print(e)
        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html',{"query":'Enter a valid query'})


# Define a view function for the login page

def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')

    # Render the login page template (GET request)
    # welcome_message = f"Welcome, {request.user.username}!" if request.user.is_authenticated else ""
    # return render(request, 'login.html', {'welcome_message': welcome_message})
    return render(request, 'login.html')

# Define a view function for the registration page
def logout_view(request):
    logout(request)
    return redirect('/login/')

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')

    # Render the registration page template (GET request)
    return render(request, 'register.html')

@login_required
def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        print(user)
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user.id)
    return render(request, 'index.html', {'foods': foods, 'consumed_food': consumed_food})

@login_required
def delete_item(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/index/')
    return render(request, 'delete.html')