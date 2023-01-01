from django.shortcuts import render,get_object_or_404
from .models import Tag,Post,Author
from django.http import HttpResponse
# Create your views here.
def post(request,slug):
    posts=get_object_or_404(Post,slug=slug)
    return render(request,"blog/post.html",{
        "posts":posts,
    })

def index(request):
    posts=Post.objects.all()
    return render(request,"blog/index.html",{
        "posts":posts
    })

def mainPage(request):
    return render(request,"blog/mainPage.html")