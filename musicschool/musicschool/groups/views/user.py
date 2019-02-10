from django.views.generic.base import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


class RegistrationView(View):
    template_name = "registration/signup.html"

    def post(self, request):
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

        