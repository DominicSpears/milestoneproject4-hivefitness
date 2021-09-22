from django.shortcuts import render, get_object_or_404
from .models import Post, Postcategory
from .forms import PostForm

# Create your views here.


def all_posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()
    postcategories = None

    if request.GET:
        if 'postcategory' in request.GET:
            postcategories = request.GET['postcategory'].split(',')
            posts = posts.filter(postcategory__name__in=postcategories)
            postcategories = Postcategory.objects.filter(name__in=postcategories)

    context = {
        'posts': posts,
        'current_postcategories': postcategories,
    }

    return render(request, 'posts/posts.html', context)


def post_detail(request, post_id):
    """ A view to show individual post details """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'posts/post_detail.html', context)


def add_post(request):
    """ Add a post to the blog page """
    form = PostForm()
    template = 'posts/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
