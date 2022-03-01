from django.contrib import admin
from blog.models import Post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'author', 'title', 'content', 'status', 'published_date', 'created_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    # exclude = ('content',)
    # fields = ('content', 'title')
admin.site.register(Post, postAdmin)