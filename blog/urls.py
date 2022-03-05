from django.urls import URLPattern, path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", blog_view, name='index'),
    path("<int:pid>", single_view, name='single'),
    path("test/<str:name>/<str:family_name>/<int:age>/<int:pid>", test, name='test'),
    path("test/", test_function, name="test-page"),
    path("category/<str:cat_name>", blog_view, name="category"),
    path("writer/<str:writer_username>", blog_view, name='writer')
]