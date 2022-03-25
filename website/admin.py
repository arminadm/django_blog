from xml.etree.ElementTree import Comment
from django.contrib import admin
from website.models import Contact, newsLetter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    empty_value_display = '-empty-'
    list_display = ['name', 'subject', 'email', 'created_time']
    list_filter = ('email',)
    search_fields = ['name', 'email', 'subject', 'message']
admin.site.register(Contact, ContactAdmin)

class newsLetterAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    list_display = ['email', 'created_time']
    search_fields = ['email']
admin.site.register(newsLetter, newsLetterAdmin)
