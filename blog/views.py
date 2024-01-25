from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

posts=[
    {
        'author':"Ayush",
        'title':"First Post",
        'content':"My first post ever!!!",
        'date_posted':"05-01-2024"
    },
    {
        'author':"Luigi",
        'title':"Second Post",
        'content':"Mamma Miaaa",
        'date_posted':"06-01-2024"
    }
]

def home(request):
    return render(request, "blog/home.html",{
        'posts':Post.objects.all()
    })

def about(request):
    return render(request, "blog/about.html",{
        'title': 'About Page'
    })