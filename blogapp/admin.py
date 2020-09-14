from django.contrib import admin

# Register your models here.
from blogapp.models import Blogs
from portfolioapp import models

admin.site.register(Blogs)
admin.site.register(models.BloggerBlogs)
