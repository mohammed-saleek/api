from django.urls import path,include
from . import views

urlpatterns = [
    path('create_blog',views.create_blog,name='create_blog'),
    path('listing_blogs',views.listing_blogs,name='listing_blogs'),
    path('view_blog/<str:pk>',views.view_blog,name ='view_blog'),
    path('remove_blog/<str:pk>',views.remove_blog,name='remove_blog'),
    path('update_blog/<str:pk>',views.update_blog,name='update_blog'),
    path('update_whole_blog/<str:pk>',views.update_whole_blog,name='update_whole_blog'),
]