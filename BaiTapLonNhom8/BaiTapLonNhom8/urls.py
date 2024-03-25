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
from my_profile import views as myProfile
from django.conf.urls.static import static
from django.conf import settings
from blogapp import views as blogapp
from loading import views as loading
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loading.get_loading, name='loading'),
    path('home/',home.get_home, name='home'),
    path('login/',login.get_login, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('login/authenticate/', login.authenticate_user, name='authenticate_user'),
    path('register/',register.get_register, name='register'),
    path('contact/',contact.get_contact, name='contact'),
    path('blog/',blog.get_blog, name='blog'),
    path('blog/create/', blog.create_blog, name='create_blog'),
    path('blog/<int:blog_id>/', blog.blog_detail, name='blog_detail'),
    path('edit/<int:blog_id>/', blog.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', blog.delete_blog, name='delete_blog'),
    path('blog/<int:blog_id>/add_comment/', blog.add_comment, name='add_comment'),
    path('profile/', myProfile.user_profile, name='profile'),
    path('blogapp/', blogapp.get_blogapp, name='blog_app'),
    path('accounts/', include('allauth.urls')),
    path('login_with_facebook/', login.login_with_facebook, name='login_with_facebook'),
    path('facebook/', login.get_facebook, name='facebook'),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
