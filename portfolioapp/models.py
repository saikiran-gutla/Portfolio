from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BloggerBlogs(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_description = models.TextField(max_length=500)
    blog_profile_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                          default="Anonymous")
    blog_date = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField(upload_to="blogapp/images")
    blog_url = models.URLField(blank=True)

    def __str__(self):
        return self.blog_title
