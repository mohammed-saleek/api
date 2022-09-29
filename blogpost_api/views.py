from dataclasses import fields
from django.shortcuts import render

from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .serializers import *
# Create your views here.

@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
