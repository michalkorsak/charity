from django.contrib import messages, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import UserManager, User
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from charity import models
from .forms import UserCreationFormExtended, LoginForm
from .models import Donation, Category, Institution

# Create your views here.
from django.views import View


    
class LandingPage(View):

    def get(self, request):
        quantity = Donation.objects.only('quantity')
        institutions = Institution.objects.filter(type=1)
        institutions1 = Institution.objects.filter(type=2)
        institutions2 = Institution.objects.filter(type=3)
        context = {'quantity': quantity,
                   'institutions': institutions,
                   'institutions1': institutions1,
                   'institutions2': institutions2}
        return render(request, 'index.html', context)


class AddDonation(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login.html/')
        else:
            categories = Category.objects.all()
            institutions = Institution.objects.all()
            return render(request, 'form.html', {'categories': categories,
                                                 'institutions': institutions})


class Register(View):

    def get(self, request):
        form = UserCreationFormExtended()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            u = form.save()
            login(request, u)
            return redirect('/')
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
            form.add_error('password', ['Błędne hasło.'])
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class Profile(View):

    def get(self, request):
        return render(request, "user_profile.html")


class InstitutionList(View):
    def get(self, request):
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'institutions': institutions})

