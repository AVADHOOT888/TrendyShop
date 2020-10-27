from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="BlogHome"),
path('blogPost/<int:id>', views.blogPost, name="blogHome")
]