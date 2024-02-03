from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'thumnail', 'detail']
        widgets = {
            'detail': forms.Textarea(attrs={'rows': 10}),  
        }