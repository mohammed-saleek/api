from rest_framework import serializers
from .models import *

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        