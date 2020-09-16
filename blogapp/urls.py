from django.urls import path

from blogapp.views import home, detail_blog,edit_blog
app_name = 'blogs'
urlpatterns = [
    path('', home, name='home'),
    path('<int:blog_id>', detail_blog, name='detail_blog'),
    path('edit/<int:blog_id>', edit_blog, name='edit_blog'),
]
