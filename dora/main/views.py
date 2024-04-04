from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from django.shortcuts import render, redirect

from .forms import RegisterForm, SampleModelForm, LoginForm
from .models import VisitedPage


def index(request):
    response = render(request, 'glav.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def create(request):
    if request.method =='POST':
        form = SampleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boot')
    else:
        form = SampleModelForm()

    return render(request, 'register.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        visited_pages = []
        visited_cookies = request.COOKIES.get('visit_count')
        if visited_cookies:
            visited_pages = visited_cookies.split(',')
            for page in visited_pages:
                VisitedPage.objects.create(user=request.user, page_name=page)
            response = redirect('create_form')
            response.delete_cookie('visit_count')
            return response
    else:
        return redirect('create_form')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль. Пожалуйста, попробуйте снова.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
