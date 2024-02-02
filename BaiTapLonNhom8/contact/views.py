from django.shortcuts import render
from .forms import ContactForm

def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Phản hồi của bạn đã được gửi thành công!"
        else:
            message = "Đã có lỗi xảy ra. Vui lòng kiểm tra lại thông tin và thử lại."
    else:
        form = ContactForm()
        message = None
    return render(request, 'contact.html', {'form': form, 'message': message})



