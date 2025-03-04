# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    priority = models.CharField(
        max_length=10, 
        choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    )
    notes = models.TextField(blank=True, null=True)  # New notes field
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"
