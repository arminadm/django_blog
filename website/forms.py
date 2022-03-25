from django import forms
from website.models import Contact, newsLetter
from captcha.fields import CaptchaField
'''using form by models.model'''
# class NameForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=255)
#     message = forms.CharField(widget=forms.Textarea)

class contactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class newsLetterForm(forms.ModelForm):
    class Meta:
        model = newsLetter
        fields = '__all__'