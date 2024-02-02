from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def get_register(request):
    message = None
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Tạo thông báo thành công
            message = "Tài khoản đã được đăng ký thành công!"
        else:
            # Lấy danh sách các lỗi từ form
            message = "Đã có lỗi xảy ra:"
            for field, errors in form.errors.items():
                for error in errors:
                    message += f"\n- {field}: {error}"
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form, 'message': message})

