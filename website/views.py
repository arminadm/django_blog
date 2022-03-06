from django.shortcuts import render
from django.http import HttpResponse
from website.models import Contact
# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, "website/about.html")

def contact_view(request):
    return render(request, "website/contact.html")

def testFrom(request):
    if request.method == 'GET':
        return render(request, 'testForm.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)
        c = Contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
        return HttpResponse('done')