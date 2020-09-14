from django.urls import path

from portfolioapp.views import *

urlpatterns = [
    path('blogger_homepage', blogger_homepage, name='blogger_homepage'),
]
