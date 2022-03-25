from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'website'
        verbose_name = 'مخاطبین'
        verbose_name_plural = 'مخاطبین'
        ordering = ['-created_time']
    def __str__(self):
        return self.subject

class newsLetter(models.Model):
    email = models.EmailField(max_length=254)
    created_time = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.email
