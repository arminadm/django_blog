from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def single_view(request):
    return render(request, "blog/blog-single.html")

def test(request, name, family_name, age, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post, 'name': name, 'family_name': family_name, 'age': age}
    return render(request, 'test.html', context)