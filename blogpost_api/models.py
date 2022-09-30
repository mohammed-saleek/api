from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Blog(models.Model):
    blog_name = models.CharField(max_length=100,blank=True,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.blog_name