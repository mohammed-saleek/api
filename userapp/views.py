from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse #To send json response

from .serializers import UserRegistrationSerializer

# from userapp import serializers

# Create your views here.

@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered a new user"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)
