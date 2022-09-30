from dataclasses import fields
from django.shortcuts import render

from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response

from .serializers import *

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
    return Response(serializer.data)
