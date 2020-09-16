import os
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from blogapp.models import Blogs
from django.core.files.storage import FileSystemStorage

# Create your views here.
from portfolioapp.decorators import is_user_unauthenticated
from portfolioapp.models import BloggerBlogs


def home(request):
    all_blogs = BloggerBlogs.objects.all()
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


@login_required(login_url='login')
def write_blog(request):
    if request.method == "POST" and request.FILES['blog_image']:
        blog_title_name = request.POST.get('title_name')
        blog_image = request.POST.get('blog_image')
        blog_description = request.POST.get('blog_description')
        author_name = request.POST.get('blogger_name')
        print(f"Blog Title name : {blog_title_name}")
        print(f"Blog Image : {blog_image}")
        print(f"Blog Description : {blog_description}")
        print(f"Blog Author : {author_name}")
        myfile = request.FILES['blog_image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(f"FIle Nae : {filename}")
        # uploaded_file_url = fs.url(filename)
        # print(f"File Url : {uploaded_file_url}")
        blog_usr = User.objects.get(username=author_name)
        print(f"blog user : {blog_usr}")
        blog = BloggerBlogs(blog_title=blog_title_name, blog_description=blog_description,
                            blog_image=filename)
        blog.blog_profile_name = blog_usr
        print(f"Before saving {blog}")
        blog.save()
        print(f"After saving {blog}")
        return render(request, 'blogapp/home.html', {
            'uploaded_file_url': filename})
    else:
        return render(request, 'portfolioapp/create_blog.html', {})


@login_required(login_url='login')
def update_blog(request, blog_id):
    if request.method == "POST":
        blog_title_name = request.POST.get('title_name')
        blog_image = request.POST.get('blog_image')
        blog_description = request.POST.get('blog_description')
        author_name = request.POST.get('blogger_name')
        filename = ""
        print(f"Blog Title name : {blog_title_name}")
        print(f"Blog Image : {blog_image}")
        print(f"Blog Description : {blog_description}")
        print(f"Blog Author : {author_name}")
        blog_usr = User.objects.get(username=author_name)
        print(f"blog user : {blog_usr}")
        blog = BloggerBlogs.objects.get(pk=blog_id)
        blog.blog_title = blog_title_name
        blog.blog_profile_name = blog_usr

        if blog_description is not None:
            blog.blog_description = blog_description
        if blog_image != "":
            myfile = request.FILES['blog_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            blog.blog_image = filename
            print(f"FIle Nae : {filename}")

        print(f"Before saving {blog}")
        blog.save()
        print(f"After saving {blog}")
        messages.success(request, "Blog Updated Successfully")
        return render(request, 'blogapp/home.html', {
            'uploaded_file_url': filename})
    else:
        return render(request, 'blogapp/edit_blog.html', {})


@login_required(login_url='login')
def user_blogs(request):
    if request.method == "GET":
        blog_data = BloggerBlogs.objects.filter(blog_profile_name=request.user)
        # blog_data = get_object_or_404(BloggerBlogs, blog_profile_name=user_name)
        return render(request, 'blogapp/home.html', context={'All_Blogs': blog_data})


def user_detail_blog(request, blog_id):
    blog_data = get_object_or_404(BloggerBlogs, pk=blog_id)
    return render(request, 'blogapp/blog_detail.html', context={'blog': blog_data})


def logout_user(request):
    auth.logout(request)
    return redirect('login')
