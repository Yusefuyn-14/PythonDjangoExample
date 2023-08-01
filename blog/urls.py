from django.urls import path
from . import views
# http://127.0.0.1:8000/

urlpatterns=[
    path('',views.index,name="home"),
    path('index',views.index),
    path('blogs',views.blog,name="blog"),
    path('blogs/<slug:slug_field>',views.blog_details,name="blog_details"),
    path('referance',views.referance,name="referance"),
]