from django.urls import path

from portfolioapp.views import *

urlpatterns = [
    path('blogger_homepage', blogger_homepage, name='blogger_homepage'),
    path('write_blog', write_blog, name='write_blog'),
    path('user_blogs', user_blogs, name='user_blogs'),
    path('<int:blog_id>', user_detail_blog, name='user_detail_blog'),
    path('update/<int:blog_id>', update_blog, name='update_blog'),
]
