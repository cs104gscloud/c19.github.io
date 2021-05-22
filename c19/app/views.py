from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account, Covid
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app/index.html', {
        'title': 'Home',
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('slogin')
        else:
            messages.error(request, 'Check your username and password')
            return redirect('login')
    return render(request,'app/login.html', {
        'title': 'Login',
    })

def archive_news(request):
    return render(request, 'app/archive-news.html', {
        'title': 'Archive news',
    })

def contact(request):
    return render(request, 'app/contact.html', {
        'title': 'Contact',
    })

def donation(request):
    return render(request, 'app/donation.html', {
        'title': 'Donation',
    })

def faq(request):
    return render(request, 'app/faq.html', {
        'title': 'Faq',
    })

def infected(request):
    return render(request,'app/infected.html', {
        'title': 'Infected',
    })

def predictions(request):
    covid = Covid.objects.get(user=request.user)
    return render(request,'app/predictions.html', {
        'title': 'Predictions',
        'dry': covid.dry,
        'fever': covid.fever,
        'throat': covid.throat,
        'difficulty': covid.difficulty,
    })

def protection(request):
    return render(request, 'app/protection.html', {
        'title': 'Protection',
    })

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        doctor = request.POST.get('doctor', False)
        phone = request.POST['phone']
        register_permission = True
        if password != password2:
            register_permission = False
            messages.error(request, 'Passwords don\'t match.')
        if User.objects.filter(email=email).exists():
            register_permission = False
            messages.error(request, 'Email already exists.')
        if User.objects.filter(username=username).exists():
            register_permission = False
            messages.error(request, 'Username already exists.')
        if register_permission:
            user = User.objects.create(username=username, email=email, password=password)
            Account.objects.create(phone=int(phone), doctor=bool(doctor), user=user)
            login(request, user)
            return redirect('slogin')
        else:
            return redirect('register')
    return render(request, 'app/signup.html', {
        'title': 'Register',
    })

def single_news(request):
    return render(request, 'app/single-news.html', {
        'title': 'Single news',
    })

def slogin(request):
    if request.method == 'POST':
        dry = int(request.POST['dry'])
        fever = int(request.POST['fever'])
        throat = int(request.POST['throat'])
        difficulty = int(request.POST['difficulty'])
        Covid.objects.create(dry=dry, fever=fever, throat=throat, difficulty=difficulty, user=request.user)
        return redirect('predictions')
    return render(request, 'app/slogin.html', {
        'title': 'Prediction',
    })

def logout_view(request):
    logout(request)
    return render(request, 'app/logout.html', {
        'title': 'Logout',
    })