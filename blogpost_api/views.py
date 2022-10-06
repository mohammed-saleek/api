from dataclasses import fields
from functools import partial
from django.shortcuts import render

from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response

from .serializers import *

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#Creating a blog
@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
    return Response(serializer.data)

#To list blogs based on the user logged in
@api_view(['GET'])
def listing_blogs(request):
    try:
        blogs = Blog.objects.filter(owner=request.user)
    except Blog.DoesNotExist:
        blogs = None
    serializer = BlogSerializers(blogs, many=True)
    return Response(serializer.data)

#To get a single blog for a user
@api_view(['GET'])
def view_blog(request,pk):
    try:
        blog = Blog.objects.get(id=pk,owner=request.user)
        serializer = BlogSerializers(blog)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        data = {}
        data['Blog_name'] = "No such blog in your directory"
        return Response(data)
    
#To delete a blog belonging to a particular user
@api_view(['DELETE'])
def remove_blog(request,pk):
    try:
        blog = Blog.objects.get(id=pk,owner=request.user)
        blog.delete()
        return Response("Blog has been deleted")
    except Blog.DoesNotExist:
        return Response("Cannot find a blog for this user with this ID")

#To Update a blog belonging to a particular user
@api_view(['PATCH'])
def update_blog(request,pk):
    try:
        blog = Blog.objects.get(id=pk,owner=request.user)
    except Blog.DoesNotExist:
        blog = None
        return Response("Cannot find a blog for this user with this ID")
    serializer = BlogSerializers(data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Invalid Data")
        