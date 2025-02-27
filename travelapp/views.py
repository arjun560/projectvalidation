from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def fyp(request):
    return render(request,'fyp.html')

def service(request):
    return render(request,'service.html')

def login(request):
    return render(request,'login.html')

def recomendations(request):
    return render(request,'recomendations.html')

def contact(request):
    return render(request,'contact.html')

def userdash(request):
    return render(request,'userdash.html')

def favlocation(request):
    return render(request,'favlocation.html')

def recentrecom(request):
    return render(request,'recentrecom.html')

def support(request):
    return render(request,'support.html')

def testimonial(request):
    return render(request,'testimonial.html')

def profile(request):
    return render(request,'profile.html')

#user registration
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Register view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirmpassword = request.POST.get('confirmpassword', '')

        if not all([username, email, password, confirmpassword]):
            messages.error(request, 'Please fill all the fields.')
        elif password != confirmpassword:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login_view')

    return render(request, 'login.html', {'page': 'register'})


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('index')  # Adjust 'index' to the name of your home page view
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'page': 'login'})
