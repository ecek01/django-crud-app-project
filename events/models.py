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
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # New color field
    COLOR_CHOICES = [
        ('#FF5733', 'Red'),
        ('#33FF57', 'Green'),
        ('#3357FF', 'Blue'),
        ('#FF33A8', 'Pink'),
        ('#FFC300', 'Yellow'),
        ('#A833FF', 'Purple'),
        ('#33FFF3', 'Cyan'),
    ]
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#FF5733')  # Default Red

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"

