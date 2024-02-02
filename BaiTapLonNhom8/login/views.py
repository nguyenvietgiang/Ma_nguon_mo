from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def get_login(request):
    # Hiển thị trang đăng nhập
    return render(request, 'login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Chuyển hướng đến trang chính sau khi đăng nhập thành công
        else:
            return render(request, 'login.html', {'error': 'Tên đăng nhập hoặc mật khẩu không đúng'})
    else:
        return redirect('login')  # Nếu là request GET, chuyển hướng lại đến trang đăng nhập
        
def logout_view(request):
    # Đăng xuất người dùng
    logout(request)
    return redirect('login')
