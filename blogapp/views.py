from django.shortcuts import render, get_object_or_404
from .models import Blogs
from portfolioapp.models import BloggerBlogs


# Create your views here.
def home(request):
    blogs_data = BloggerBlogs.objects.all()
    return render(request, 'blogapp/home.html', context={'All_Blogs': blogs_data})


def detail_blog(request, blog_id):
    blog_data = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blogapp/blog_detail.html', context={'blog': blog_data})


def edit_blog(request, blog_id):
    blog_data = get_object_or_404(BloggerBlogs, pk=blog_id)
    return render(request, 'blogapp/edit_blog.html', context={'blog': blog_data})
