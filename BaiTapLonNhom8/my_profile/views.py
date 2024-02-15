from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Blog

@login_required(login_url='login') 
def user_profile(request):
    # Lấy thông tin của người dùng đang đăng nhập
    user = request.user
    # Lấy danh sách các blog của người dùng
    user_blogs = Blog.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user': user, 'user_blogs': user_blogs})