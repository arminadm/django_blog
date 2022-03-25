from django.urls import URLPattern, path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('rss/feed/', LatestEntriesFeed()),
    path("", blog_view, name='index'),
    path("<int:pid>", single_view, name='single'),
    path("test/<str:name>/<str:family_name>/<int:age>/<int:pid>", test, name='test'),
    path("test/", test_function, name="test-page"),
    path("category/<str:cat_name>", blog_view, name="category"),
    path("writer/<str:writer_username>", blog_view, name='writer'),
    path("search/", search_func, name='search'),
    path("tag/<str:tag_name>", blog_view, name='tag'),
]