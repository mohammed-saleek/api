from django.urls import path,include
from .import views

urlpatterns = [
    path('user_registration',views.registration,name = 'registration'),
]