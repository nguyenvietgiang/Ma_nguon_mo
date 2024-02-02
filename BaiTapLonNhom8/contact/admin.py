from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at') 
    list_filter = ('created_at',) 
    search_fields = ('name', 'email')  

admin.site.register(Contact, ContactAdmin)
