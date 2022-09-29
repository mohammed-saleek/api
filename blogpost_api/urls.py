from django.urls import path,include
from . import views

urlpatterns = [
    path('create_blog',views.create_blog,name='create_blog'),
]