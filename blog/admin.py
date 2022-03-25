from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class postAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'author', 'title', 'status', 'published_date', 'created_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    # exclude = ('content',)
    # fields = ('content', 'title')
    summernote_fields = ('content',)
admin.site.register(Post, postAdmin)

class categoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, categoryAdmin)

class commentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    empty_value_display = '-empty-'
    list_display = ('post',  'author', 'approved', 'created_time')
    list_filter = ('approved',)
    search_fields = ['post', 'author', 'email', 'created_time']
admin.site.register(Comment, commentAdmin)