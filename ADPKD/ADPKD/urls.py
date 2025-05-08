"""
URL configuration for ADPKD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ADPKD import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name="home"),
    path('About_Us/',views.About_Us,name="About_Us"),
    path('GFR/',views.GFR,name="GFR"),
    path('Doctors/',views.Doctors,name="Doctors"),
    path('Blogs/', views.Blogs, name='Blogs'),
   path('appointment-confirmed/<uuid:appointment_id>/',
         views.appointment_confirmed, name='appointment_confirmed'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('ChatBot/', views.chatbot_page, name='ChatBot'),
    path("chatbot-response/",views.chatbot_response, 
         name="chatbot_response"),
    path("autocomplete-suggestions/",views.autocomplete_suggestions, 
         name="autocomplete_suggestions"),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path("reset-password/", views.password_reset_request, name="password_reset"),
    path("reset-password/<uidb64>/<token>/", views.reset_password, name="password_reset_confirm"),
    path("reset-password/complete/", views.password_reset_complete, name="password_reset_complete"),
    path('add-profile-picture/', views.add_profile_picture, name='add_profile_picture'),
    path("profile/", views.profile_view, name="profile"),
    path("ADPKD/", views.ADPKD, name="ADPKD"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
