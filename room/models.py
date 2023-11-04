from django.db import models

from core.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ('-date_added',)

class Message(models.Model):
    room = models.ForeignKey(Room,related_name="messages",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="author",on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"on room {self.room},{self.content} by {self.user} on {self.date_added}"
    class Meta:
        ordering = ('date_added',)
    
    
