from django.shortcuts import render

# Create your views here.
def get_blogapp(request):
    return render(request,'blogapp.html') 