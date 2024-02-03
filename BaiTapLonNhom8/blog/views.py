from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  
from .models import Blog
from .forms import BlogForm

def get_blog(request):
    return render(request, 'blog.html')

@login_required(login_url='login')  # Thêm decorator này
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # Lưu bài viết mới với thông tin của người dùng đăng nhập
            blog = form.save(commit=False)
            blog.user = request.user  # Gán người dùng hiện tại là người tạo bài viết
            blog.save()
            return redirect('blog_detail', blog_id=blog.id)  # Chuyển hướng đến trang chi tiết bài viết
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

