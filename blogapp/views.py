from django.shortcuts import render, get_object_or_404
from .models import Blogs


# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')


def detail_blog(request, blog_id):
    blog_data = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blogapp/blog_detail.html', context={'blog': blog_data})
