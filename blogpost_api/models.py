from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blog_name = models.CharField(max_length=100,blank=True,null=True),
    owner = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE),
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.blog_name