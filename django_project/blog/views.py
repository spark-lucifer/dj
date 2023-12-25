from django.shortcuts import render
posts=[
    {
        'author':'Corey',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'Jane',
        'title':'Blog Post 2',
        'content':'second post content',
        'date_posted':'August 28, 2018'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def About(request):
    return render(request,'blog/about.html')