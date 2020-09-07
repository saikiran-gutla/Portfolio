from django.db import models


# Create your models here.
class Blogs(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_description = models.TextField(max_length=500)
    blog_author = models.CharField(max_length=200, default="Anonymous")
    blog_date = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField(upload_to="blogapp/images")
    blog_url = models.URLField(blank=True)
    # class Meta:

