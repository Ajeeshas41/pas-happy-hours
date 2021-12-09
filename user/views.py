from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'user/login.html'
    authentication_form = UserLoginForm
    success_message = 'Succesfully Logged In'

def register_user(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            messages.success(request, f'Account created for {firstname} {lastname}!')
            new_user = authenticate(username = username,
                                    password=form.cleaned_data.get('password1'),
                                    )
            login(request, new_user)
            return redirect('setup-team')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})