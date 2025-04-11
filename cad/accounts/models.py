from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    OCCUPATION_CHOICES = [
        ('police', 'Police'),
        ('doctor', 'Doctor'),
        ('paramedic', 'Paramedic'),
        ('lawyer', 'Lawyer'),
        ('business', 'Business Person'),
    ]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhaar_number = models.CharField(max_length=12)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)  # ✅ Add this
    occupation = models.CharField(max_length=50)
    address = models.TextField()
    profile_picture_url = models.URLField()

    def __str__(self):
        return self.user.username
    
