from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag(name='plustwo')
def sum(a=2):
    return a + 2

@register.simple_tag()
def post_counter():
    posts = Post.objects.filter(status=1)
    amount = posts.count()
    return amount

@register.simple_tag()
def allowed_posts():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter()
def snippet(content, limit=20):
    return content[:limit] + '...'

@register.inclusion_tag('blog/latestposts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/post-categories.html')
def postcategories():
    categories = Category.objects.all()
    posts = Post.objects.filter(status=1)
    category_dict = {}
    for cat in categories:
        category_dict[cat] = posts.filter(category=cat).count()
    return {'categories': category_dict}