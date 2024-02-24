from django.shortcuts import render

def get_loading(request):
    return render(request,'loading.html') 