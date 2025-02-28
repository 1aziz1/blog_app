from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if an author got deleted , all the post written by that specific author will be deleted too
    created_at = models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    