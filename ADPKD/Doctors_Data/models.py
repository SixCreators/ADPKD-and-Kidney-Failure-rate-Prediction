from django.db import models
from tinymce.models import HTMLField
import random
import uuid
from django.utils.timezone import now
class Our_Doctors(models.Model):
    Dr_id = models.AutoField(primary_key=True)
    Doctors_images = models.ImageField(upload_to='Doctors_images/')
    Dr_websiteLink = models.URLField(max_length=800)  # URL field for storing website links
    Name = models.CharField(max_length=300)
    occupation = models.CharField(max_length=500)
    Location = models.CharField(max_length=300)
    Paragraph = models.CharField(max_length=300)

    def __str__(self):
        return self.Name
    
class doctor_appointment_img(models.Model):
    Dr_Ap_id = models.AutoField(primary_key=True)
    Dr_Ap_img = models.ImageField(upload_to='Dr_appointment_img/')
    description = HTMLField(blank=True,null=True)
    def __str__(self):
        return str(self.Dr_Ap_id)
    
def generate_random_id():
    return random.randint(100000, 999999)  # Generates a 6-digit random number

class Dr_Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=300)
    appointment_date = models.DateTimeField(default=now)  # Ensures correct timezone handling

    def __str__(self):
        return f"{self.name} - {self.appointment_date}"
# Create your models here.
