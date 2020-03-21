from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 

def home(request):
    if(str(request.user)!="AnonymousUser"):
        return render(request, 'base/home.html', {})
    else:
        return render(request, 'base/index.html', {})