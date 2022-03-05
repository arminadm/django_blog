from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    '''category search scenario'''
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    '''post writer search scenario'''
    if kwargs.get('writer_username') != None:
        posts = posts.filter(author__username=kwargs['writer_username'])
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post': post}
    return render(request, "blog/blog-single.html", context)

def test(request, name, family_name, age, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post, 'name': name, 'family_name': family_name, 'age': age}
    return render(request, 'test.html', context)

def test_function(request):
    return render(request, 'test2.html')