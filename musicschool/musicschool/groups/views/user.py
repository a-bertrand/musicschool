from django.views.generic.base import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from musicschool.groups.models import ERPUser


class RegistrationView(View):
    template_name = "registration/signup.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            erp_user = ERPUser(
                phonenumber=request.POST['phone'],
                adress=request.POST['adress'],
                user=user
            )
            user.save()
            erp_user.save()
            
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()


