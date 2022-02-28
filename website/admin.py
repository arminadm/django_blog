from django.contrib import admin
from website.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    empty_value_display = '-empty-'
    list_display = ['name', 'subject', 'email', 'created_time']
    list_filter = ('email',)
    search_fields = ['name', 'email', 'subject', 'message']
admin.site.register(Contact, ContactAdmin)