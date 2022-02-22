from django.urls import URLPattern, path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", blog_view, name='index'),
    path("single/", single_view, name='single')
]