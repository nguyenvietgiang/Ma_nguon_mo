"""
URL configuration for BaiTapLonNhom8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views as home
from login import views as login
from register import views as register
from contact import views as contact
from blog import views as blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.get_home, name='home'),
    path('login/',login.get_login, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('login/authenticate/', login.authenticate_user, name='authenticate_user'),
    path('register/',register.get_register, name='register'),
    path('contact/',contact.get_contact, name='contact'),
    path('blog/',blog.get_blog, name='blog'),
]
