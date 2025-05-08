from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Primary key
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    Name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=[("male", "Male"), ("female", "Female")])
    Phone_Number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.user.username} - {self.Name}"  # Returns User ID and Username
# Create your models here.