from django.conf import settings
from django.db import models
import datetime
from django.utils import timezone
from PIL import Image

class Todo(models.Model):
    LEVEL_OF_IMPORTANCE = (
            ('!', 'Low'),
            ('!!', 'Medium'),
            ('!!!', 'High'),
        )
    
    title = models.CharField(max_length=50, unique_for_date="due_date")
    body = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True,blank=True)
    importance = models.CharField(max_length=3, choices=LEVEL_OF_IMPORTANCE)
    finished = models.BooleanField(default=False) 
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_todos')
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_with_me') 
    time_since_modified = models.DateTimeField(auto_now=True)
    user_last_change = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lastly_changed', null=True)
    image = models.ImageField(default='todo.jpeg',upload_to='todo_attachments')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        
        if img.height > 100 or img.width > 100:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg',
            upload_to='profile_images')
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (200,200)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

