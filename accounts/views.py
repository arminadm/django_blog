from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = messages.add_message(request, messages.ERROR, 'Failed to logged in')
                return redirect('/account/login')
        else:
            message = messages.add_message(request, messages.ERROR, 'username or password is not correct')
            return redirect('/account/login')

    if request.method == 'GET':
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
            else:
                form = UserCreationForm()
                errors = [
                    'required 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                    'Your password can’t be too similar to your other personal information.',
                    'Your password must contain at least 8 characters.',
                    'Your password can’t be a commonly used password.',
                    'Your password can’t be entirely numeric.'
                    
                ]
                context = {'form': form, 'errors': errors}
                return render(request, 'accounts/signup.html', context)
        if request.method == 'GET':
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
