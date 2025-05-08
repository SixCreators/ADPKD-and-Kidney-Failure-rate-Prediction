from django.db import models
from tinymce.models import HTMLField
from datetime import date  # Import date

class Kidney_Anatomy(models.Model):
    title = models.CharField(max_length=255)
    Kidney_Anatomy_image = models.ImageField(upload_to='kidney_blood_flow_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    

class kidney_blood_flow(models.Model):
    title = models.CharField(max_length=255)
    kbf_images = models.ImageField(upload_to='kidney_blood_flow_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class HKVSDK(models.Model):
    title = models.CharField(max_length=255)
    HKVSDK_images = models.ImageField(upload_to='HKVSDK_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class CKD(models.Model):
    title = models.CharField(max_length=255)
    CKD_images = models.ImageField(upload_to='CKD_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class PKD(models.Model):
    title = models.CharField(max_length=255)
    PKD_images = models.ImageField(upload_to='PKD_images/')
    description = HTMLField()

    def __str__(self):
        return self.title
    
class slider_section(models.Model):
    SI_id = models.AutoField(primary_key=True)
    SI_images = models.ImageField(upload_to='SI_images/')
    description = HTMLField(blank=True,null=True)

    def __str__(self):
        return str(self.SI_id)
    
class Reference(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key
    Paragraph = models.CharField(max_length=500)  # A simple text field
    websiteLink = models.URLField(max_length=800)  # URL field for storing website links
    Check_Orginal =models.CharField(max_length=500)
    created_date = models.DateField(default=date.today)  # Date field

    def __str__(self):
        return f"{self.id} - {self.Paragraph}"  # Display ID and name in admin panel
    
class home_top_content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class home_top_img(models.Model):
    id = models.AutoField(primary_key=True)
    Home_Top_images = models.ImageField(upload_to='Home_Top_images/')
    description = HTMLField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
    
class card_section(models.Model):
    Card_id = models.AutoField(primary_key=True)
    Card_images = models.ImageField(upload_to='Card_images/',blank=True,null=True)
    Card_Name= models.CharField(max_length=255)
    Card_Link = models.URLField(max_length=500,default="www.abc.com")  # URL field

    def __str__(self):
        return str(self.Card_Name)

# Create your models here.
