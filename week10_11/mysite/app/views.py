from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .form import LoginForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = auth.authenticate(username=cd['username'], password=cd['password'])
            if user:
                auth.login(request, user)
                return redirect('/home')
            else:
                login_form.add_error('password', '用户名或密码错误')
        return render(request, 'login.html', {'form': login_form})


def logout(request):
    auth.logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')
