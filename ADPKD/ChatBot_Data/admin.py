from django.contrib import admin
from ChatBot_Data.models import ChatbotSuggestion
admin.site.register(ChatbotSuggestion)
from ChatBot_Data.models import ChatResponse
admin.site.register(ChatResponse)

# Register your models here.
