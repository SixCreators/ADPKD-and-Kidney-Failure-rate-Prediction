from django.db import models
from tinymce.models import HTMLField
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='team_pictures/')
    occupation = models.CharField(max_length=255)
    bio = models.TextField()
    
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Aboutus_TP_Data(models.Model):
    Abus_TP_Img = models.ImageField(upload_to='Abus_TP_Img/')
    First_Hedding = models.CharField(max_length=1000)
    First_Paragraph = HTMLField()
    Second_Headding = models.CharField(max_length=1000)
    Second_Paragraph = HTMLField()
    
    def __str__(self):
        return self.First_Hedding
# Create your models here.
