from rest_framework import serializers
from .models import *

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blog_name','owner','content','subscription_price','created_at']
        read_only_fields = ['owner']
        