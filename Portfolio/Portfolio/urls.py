"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from charity import views
from charity.views import LandingPage, AddDonation, Register, LoginView, LogoutView, Profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html/', LandingPage.as_view(), name="landing_page"),
    path('form.html/', AddDonation.as_view(), name="add_donation"),
    path('register.html/', Register.as_view(), name="register"),
    path("login.html/", LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
]