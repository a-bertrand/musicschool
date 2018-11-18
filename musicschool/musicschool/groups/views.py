from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from  .models import MemberGroup

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def home (request):
    if User.is_authenticated:

        return render(request, 'home.html', {'form':form})
    else:
        return redirect('login')