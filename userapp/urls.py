from django.urls import path,include
from .import views

urlpatterns = [
    path('user_registration',views.registration,name = 'registration'),
    path('user_login',views.login,name = 'login'),
]