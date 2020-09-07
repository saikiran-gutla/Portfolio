from django.urls import path

from blogapp.views import home, detail_blog
app_name = 'blogs'
urlpatterns = [
    path('', home, name='home'),
    path('<int:blog_id>', detail_blog, name='detail_blog'),
]
