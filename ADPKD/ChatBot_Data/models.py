from django.db import models
class ChatResponse(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question


class ChatbotSuggestion(models.Model):
    question = models.CharField(max_length=255)
    question_Short = models.CharField(max_length=255)

    def __str__(self):
        return self.question
# Create your models here.
