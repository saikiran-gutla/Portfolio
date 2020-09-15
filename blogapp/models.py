from django.db import models


# Create your models here.
class Blogs(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_description = models.TextField(max_length=500)
    blog_author = models.CharField(max_length=200, default="Anonymous")
    blog_date = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField()
    blog_url = models.URLField(blank=True)

    def __str__(self):
        return self.blog_title
