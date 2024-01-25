from django.shortcuts import render

posts=[
    {
        'author':"Ayush",
        'title':"First Post",
        'content':"My first post ever!!!",
        'date':"05-01-2024"
    },
    {
        'author':"Luigi",
        'title':"Second Post",
        'content':"Mamma Miaaa",
        'date':"06-01-2024"
    }
]

def home(request):
    return render(request, "blog/home.html",{
        'posts':posts
    })

def about(request):
    return render(request, "blog/about.html",{
        'title': 'About Page'
    })