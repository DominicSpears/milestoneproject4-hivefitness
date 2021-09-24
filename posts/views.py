from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Post, Postcategory
from .forms import PostForm, PostcategoryForm, CommentForm

# Create your views here.


def all_posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()
    postcategories = Postcategory.objects.all()

    if request.GET:
        if 'postcategory' in request.GET:
            postcategories = request.GET['postcategory'].split(',')
            posts = posts.filter(postcategory__name__in=postcategories)
            postcategories = Postcategory.objects.filter(name__in=postcategories)

    context = {
        'posts': posts,
        'postcategories': postcategories,
    }

    return render(request, 'posts/posts.html', context)


def post_detail(request, post_id):
    template_name = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def add_post(request):
    """ Add a post to the blog page """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('posts'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'posts/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_post(request, post_id):
    """ Edit a post in the blog """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'posts/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_post(request, post_id):
    """ Delete a post from the blog """
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('posts'))


def all_postcategories(request):
    """ A view to show all blog categorys """
    postcategories = Postcategory.objects.all()
    template = 'posts/manage_categories.html'

    context = {
        'postcategories': postcategories,
    }

    return render(request, template, context)


def add_postcategory(request):
    """ Add a post category to the blog options """
    if request.method == 'POST':
        form = PostcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post category!')
            return redirect(reverse('postcategories'))
        else:
            messages.error(request, 'Failed to add post category. Please ensure the form is valid.')
    else:
        form = PostcategoryForm()

    template = 'posts/add_postcategory.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_postcategory(request, postcategory_id):
    """ Edit a post category in the blog options """
    postcategory = get_object_or_404(Postcategory, pk=postcategory_id)
    if request.method == 'POST':
        form = PostcategoryForm(request.POST, instance=postcategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post category!')
            return redirect(reverse('postcategories'))
        else:
            messages.error(request, 'Failed to update post category. Please ensure the form is valid.')
    else:
        form = PostcategoryForm(instance=postcategory)
        messages.info(request, f'You are editing {postcategory.name}')

    template = 'posts/edit_postcategory.html'
    context = {
        'form': form,
        'postcategory': postcategory,
    }

    return render(request, template, context)


def delete_postcategory(request, postcategory_id):
    """ Delete a post category from the blog options """
    postcategory = get_object_or_404(Postcategory, pk=postcategory_id)
    postcategory.delete()
    messages.success(request, 'Post category deleted!')
    return redirect(reverse('postcategories'))
