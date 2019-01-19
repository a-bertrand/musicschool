from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from  .models import MemberGroup, Media, Article

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def home(request):
    if request.user:
        if request.user.is_staff:
            return redirect('/admin')
        elif request.user.is_authenticated:
            try:
                membergroup =  request.user.members_group.all()[0]
            except:
                membergroup = None
            return render(
                request, 
                'home.html',
                {
                    'membergroup':membergroup,
                }
            )
    else:
        return redirect('login')

def detail(request, article_id):
    if User.is_authenticated:   
        article = Article.objects.get(pk=article_id)
        membergroup =  request.user.members_group.all()[0]
        if article in membergroup.articles.all():
            return render(
                request, 
                'article_detail.html', 
                {
                    'article':article, 
                    'medias': article.media.all()
                }
            ) 
        else:
            return render(request, 'layout/not_right_page.html')
    else:
        return redirect('login')