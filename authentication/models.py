from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='books/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Track the uploader
    public = models.BooleanField(default=False)  # Visibility setting

    def __str__(self):
        return self.title
