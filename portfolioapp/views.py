from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from blogapp.models import Blogs

# Create your views here.
from portfolioapp.decorators import is_user_unauthenticated


def home(request):
    all_blogs = Blogs.objects.all()
    return render(request, 'portfolioapp/home.html', {'All_Blogs': all_blogs})


@is_user_unauthenticated
def login_user(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        print(f"User Email : {user_name}")
        print(f"User Pass1 : {user_pass}")
        dbuser = User.objects.get(username=user_name)
        dbuvalid = dbuser.check_password(user_pass)
        user = authenticate(request, username=user_name,
                            password=user_pass)
        print('***************************************', dbuser, dbuvalid)
        print(f"USER OBJECT : {user}")
        if user is not None:
            auth.login(request, user)
            return render(request, 'portfolioapp/blogger_homepage.html')
        else:
            messages.error(request, 'Invalid Login Credentials')
            return render(request, 'portfolioapp/login.html')
    else:
        return render(request, 'portfolioapp/login.html')


@is_user_unauthenticated
def signup(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_email = request.POST.get('useremail')
        user_pass1 = request.POST.get('password1')
        user_pass2 = request.POST.get('password2')
        print(f"User name : {user_name}")
        print(f"User Email : {user_email}")
        print(f"User Pass1 : {user_pass1}")
        print(f"User Pass2 : {user_pass2}")
        if user_pass1 == user_pass2:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, f"{user_name} already exists. Try Different")
                print(f"{user_name} already exists. Try Different")
                return render(request, 'portfolioapp/signup.html')
            elif User.objects.filter(email=user_email).exists():
                messages.error(request, f"{user_email} already exists. Try Different")
                print(f"{user_email} already exists. Try Different")
                return render(request, 'portfolioapp/signup.html')
            else:
                blogger = User(username=user_name,
                               email=user_email,
                               password=user_pass1,
                               )
                blogger.set_password(user_pass1)
                blogger.save()
                messages.success(request, f"{user_name} User Created")
                print(f"{user_name} User Created")
                return render(request, 'portfolioapp/login.html')
        else:
            messages.error(request, f"Passwords Mismatch")
            print(f"Password Mismatch")
            return render(request, 'portfolioapp/signup.html')

    else:
        return render(request, 'portfolioapp/signup.html', {})


@login_required(login_url='login')
def blogger_homepage(request):
    return render(request, 'portfolioapp/blogger_homepage.html', {})


def logout_user(request):
    auth.logout(request)
    return redirect('login')
