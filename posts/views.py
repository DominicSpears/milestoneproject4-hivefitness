from django.shortcuts import render
from .models import Post

# Create your views here.

def all_posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/posts.html', context)