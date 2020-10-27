from django.shortcuts import render
from .models import Blogpost

from django.http import HttpResponse
def index(request):
    myposts = Blogpost.objects.all()
    return render(request, 'blog/index.html', {"myposts": myposts})


def blogPost(request,id):


    post=Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog/blogPost.html',{"post":post})