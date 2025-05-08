from django.db import models
class KidneyStage(models.Model):
    stage_name = models.CharField(max_length=100, unique=True)
    Kidney_Condition=models.CharField(max_length=100)
    image = models.ImageField(upload_to='kidney_stages/')
    bg_color = models.CharField(max_length=7, default="#ffffff")  # HEX color code
    
    def __str__(self):
        return self.stage_name
    
class Down_Kidney_Stage(models.Model):
    stage_name= models.CharField(max_length=100)
    reference_link = models.URLField()
    DKS_img = models.ImageField(upload_to='DKS_img/')
    KD_condition= models.CharField(max_length=100)

    def __str__(self):
        return self.stage_name
    
class CKDInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    list_items = models.TextField(help_text="Enter list items separated by a semicolon (;)")
    extra_info = models.TextField()
    reference_link = models.URLField()

    def get_list_items(self):
        return self.list_items.split(";")  # Convert list items into a Python list

    def __str__(self):
        return self.title
    
class Symptom(models.Model):
    title = models.CharField(max_length=255, default="Signs and Symptoms")
    description = models.TextField()
    symptoms_list = models.TextField(help_text="Enter symptoms separated by a semicolon (;)")

    def get_symptoms(self):
        return self.symptoms_list.split(";")  # Convert symptoms into a Python list

    def __str__(self):
        return self.title
    
class RiskFactor(models.Model):
    title = models.CharField(max_length=255, default="Risk Factors")
    description = models.TextField()
    risk_items = models.TextField(help_text="Enter risk factors separated by a semicolon (;)")
    risk_links = models.TextField(help_text="Enter corresponding links separated by a semicolon (;)", blank=True, null=True)

    def get_risk_factors(self):
        factors = self.risk_items.split(";")
        links = self.risk_links.split(";") if self.risk_links else []
        return zip(factors, links)  # Pair risk factors with their links

    def __str__(self):
        return self.title
# Create your models here.
