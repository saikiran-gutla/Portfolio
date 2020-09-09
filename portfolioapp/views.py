from django.shortcuts import render
from blogapp.models import Blogs


# Create your views here.
def home(request):
    all_blogs = Blogs.objects.all()
    return render(request, 'portfolioapp/home.html', {'All_Blogs': all_blogs})


def login(request):
    return render(request, 'portfolioapp/login.html', {})


def register(request):
    return render(request, 'portfolioapp/register.html', {})
