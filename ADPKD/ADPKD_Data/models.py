from django.db import models
class SeverityStage(models.Model):
    stage_heading = models.CharField(max_length=100)  # e.g., "Early ADPKD"
    stage_number = models.CharField(max_length=20)  # e.g., "Stage-1"
    stage_title = models.CharField(max_length=200)  # e.g., "Asymptomatic or Mild Symptoms"
    stage_image = models.ImageField(upload_to='stage_images/')  # Stores images in 'media/stage_images/'
    stage_color = models.CharField(max_length=20)  # e.g., "green"
    min_value = models.IntegerField(blank=True)  # Minimum range for this stage
    max_value = models.IntegerField(blank=True)  # Maximum range for this stage

    def __str__(self):
        return f"{self.stage_number} - {self.stage_heading}"
    
class ManagementStage(models.Model):
    title = models.CharField(max_length=255)  # e.g., "Blood Pressure Control"
    details = models.TextField()  # Store multiple details separated by a newline

    def get_details(self):
        return self.details.split("\n")  # Split details into a list
# Create your models here.
