from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=255)  
    thumnail = models.ImageField(upload_to='images', null=True, blank=True, default='default-avatar.jpg') 
    detail = models.CharField(max_length=2550)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Liên kết với model người dùng

    def __str__(self):
        return self.title

