from django.db import models
class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255)  # Section title (e.g., "User Responsibilities")
    content = models.TextField()  # Rich text field for terms content (can include HTML)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when it was added
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updates on edit

    def has_contact_link(self):
        """Check if content contains an <a> tag (contact link)."""
        return '<a href="' in self.content

    def __str__(self):
        return self.title
    

class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255, default="Privacy Policy")
    content = models.TextField()  # Store policy content as rich text
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
