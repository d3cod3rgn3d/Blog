# myblog/blog/views.py

from django.shortcuts import render
from .models import Post

def index(request):
    # Query all posts from the database
    posts = Post.objects.all()
    
    # Render the index.html template with the posts data
    return render(request, 'index.html', {'posts': posts})
