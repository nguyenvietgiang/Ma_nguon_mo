from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  
from .models import Blog
from .forms import BlogForm
from .comment_forms import CommentForm
from django.contrib import messages

def get_blog(request):
    query = request.GET.get('q')
    if query:
        # Tìm kiếm các bài viết có tiêu đề chứa từ khóa tìm kiếm
        blogs = Blog.objects.filter(title__icontains=query)
    else:
        blogs = Blog.objects.all()

    return render(request, 'blog.html', {'blogs': blogs, 'query': query}) 

@login_required(login_url='login') 
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # Lưu bài viết mới với thông tin của người dùng đăng nhập
            blog = form.save(commit=False)
            blog.user = request.user  # Gán người dùng hiện tại là người tạo bài viết
            blog.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comment_form = CommentForm()

    return render(request, 'blog_detail.html', {'blog': blog, 'comment_form': comment_form})

def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.blog = blog
                comment.save()
                messages.success(request, 'Bình luận của bạn đã được thêm.')
            else:
                messages.error(request, 'Có lỗi xảy ra khi thêm bình luận.')
        else:
            # Chuyển hướng đến trang đăng nhập
            return redirect('login')

    # Chuyển hướng trở lại trang chi tiết blog sau khi thêm bình luận
    return redirect('blog_detail', blog_id=blog_id)

@login_required(login_url='login') 
def edit_blog(request, blog_id):
    # Lấy bài viết cần chỉnh sửa từ ID
    blog = get_object_or_404(Blog, id=blog_id, user=request.user)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'edit_blog.html', {'form': form})

@login_required(login_url='login') 
def delete_blog(request, blog_id):
    # Lấy bài viết cần xóa từ ID
    blog = get_object_or_404(Blog, id=blog_id, user=request.user)
    
    if request.method == 'POST':
        blog.delete()
        return redirect('profile')

    return render(request, 'confirm_delete_blog.html', {'blog': blog})
