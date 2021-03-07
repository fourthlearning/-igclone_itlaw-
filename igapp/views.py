from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect, render)

from igapp.models import IGUser, Logined, FBuser

# user : admin pass :1234
def login(request):
    logined = Logined.objects.all()
    if request.method == 'POST':
        logined = Logined.objects.create(
            ig_username = request.POST.get('username'),
            password = request.POST.get('password'),
        )
        return redirect('index')
    context = {
        'logined': Logined,
    }
    return render(request, template_name='login.html', context={

    })
def index(request):
    context = {}
    return render(request, template_name='index.html', context={

    })
def explore(request):
    context = {}
    return render(request, template_name='explore.html', context={

    })

def profile(request):
    context = {}
    return render(request, template_name='profile.html', context={

    })

def editprofile(request):
    context = {}
    return render(request, template_name='edit-profile.html', context={

    })
def facebook(request):
    fbuser = FBuser.objects.all()
    if request.method == 'POST':
        fbuser = FBuser.objects.create(
            fb_username = request.POST.get('username'),
            password = request.POST.get('password'),
        )
        return redirect('index')
    context = {
        'fbuser': FBuser,
    }
    return render(request, template_name='facebook.html', context={

    })

def signup(request):
    iguser = IGUser.objects.all()
   
    if request.method == 'POST':
        iguser = IGUser.objects.create(
            ig_username = request.POST.get('username'),
            fullname = request.POST.get('fullname'),
            phone_number = request.POST.get('phone_number'),
            password = request.POST.get('password'),
        )
        return redirect('login')
    else:
        iguser = IGUser.objects.none()
    context = {
        'iguser': IGUser,
    }
    return render(request, template_name='signup.html', context={

    })
def my_logout(request):
    logout(request)
    return redirect('login')