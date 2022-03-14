from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import contactForm, newsLetterForm
from django.contrib import messages
# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, "website/about.html")

def contact_view(request):
    if request.method == 'GET':
        form = contactForm()
        return render(request, 'website/contact.html', {'form':form})
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.add_message(request, messages.SUCCESS, 'Ticket submitted successfully')
        else:
            message = messages.add_message(request, messages.ERROR, 'Failed to send your ticket')
        return HttpResponseRedirect('/contact')

'''using form by models.model'''
# def testFrom(request):
#     if request.method == 'GET':
#         form = NameForm()
#         return render(request, 'testForm.html', {'form':form})
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             print(name, email, subject, message)
#             return HttpResponse('done')
#         else:
#             return HttpResponse('failed')

'''using form by models.modelForm'''
def testForm(request):
    if request.method == 'GET':
        form = contactForm()
        return render(request, 'testForm.html', {'form':form})
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('failed')

def news_letter_view(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = newsLetterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')