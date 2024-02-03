from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user') 
    search_fields = ('title', 'user__username')  

admin.site.register(Blog, BlogAdmin)