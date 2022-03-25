from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Comment
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from blog.forms import commentForm
from django.contrib import messages

# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    '''category search scenario'''
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    '''post writer search scenario'''
    if kwargs.get('writer_username') != None:
        posts = posts.filter(author__username=kwargs['writer_username'])
    '''tag search scenario'''
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    '''Pagination'''
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def single_view(request, pid):
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.add_message(request, messages.SUCCESS, 'Your comment successfully added to the post')
        else:
            message = messages.add_message(request, messages.ERROR, 'failed to add your comment')
        return HttpResponseRedirect(f'/blog/{pid}')
        
    elif request.method == 'GET':
        commentform = commentForm()
        post = get_object_or_404(Post, pk=pid, status=1)
        comments = Comment.objects.filter(post=post.id, approved=True)
        context = {'post': post, 'comments': comments, 'commentForm':commentform}
        return render(request, "blog/blog-single.html", context)

def test(request, name, family_name, age, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post, 'name': name, 'family_name': family_name, 'age': age}
    return render(request, 'test.html', context)

def test_function(request):
    return render(request, 'test2.html')

def search_func(request):
    # print(request.__dict__)
    if request.method == 'GET':
        posts = Post.objects.filter(status=1)
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)