import os
import json
import joblib
import numpy as np
import pandas as pd
from collections import deque
from datetime import datetime
from django.db.models import Q
from django.conf import settings
from django.http import HttpRequest
from django.http import JsonResponse
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from sklearn.preprocessing import LabelEncoder
from django.shortcuts import get_object_or_404
from Homepage_Data.models import HKVSDK,CKD
from django.template.loader import render_to_string
from ContactMessage.models import ContactMessage
from sklearn.ensemble import RandomForestRegressor
from django.views.decorators.csrf import csrf_exempt
from Homepage_Data.models import PKD,slider_section
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from Homepage_Data.models import home_top_img,card_section
from Homepage_Data.models import Reference,home_top_content
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from Homepage_Data.models import Kidney_Anatomy,kidney_blood_flow
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

def Homepage(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None
        pass
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if full_name and email and message:  # Simple validation
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            return render(request,'success_page.html')  # Replace with your success URL
    kidney_anatomy = Kidney_Anatomy.objects.all()  # Fetch all objects from Content model
    kb_flow= kidney_blood_flow.objects.all()
    hkvsdk= HKVSDK.objects.all()
    ckd= CKD.objects.all()
    pkd= PKD.objects.all()
    Slide_Section= slider_section.objects.all()
    reference= Reference.objects.all()
    HTC= home_top_content.objects.all()
    HTI= home_top_img.objects.all()
    Card_Section= card_section.objects.all()
    Data= {
        'kidney_anatomy': kidney_anatomy,'kb_flow':kb_flow,'hkvsdk':hkvsdk,
        'ckd':ckd,'pkd':pkd,'Slide_Section':Slide_Section,'reference':reference,
        'HTC':HTC,'HTI':HTI,'Card_Section':Card_Section,
        'user': request.user,'profile': user_profile,
    }
    return render(request, 'home.html',Data)

from About_Page_Data.models import TeamMember,Aboutus_TP_Data
def About_Us(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None
        pass
    team_members = TeamMember.objects.all()  # Fetch all team members
    about_us_data = Aboutus_TP_Data.objects.all()  # Fetch all entries
    About_Data= {
        'team_members': team_members,'about_us_data':about_us_data,
        'user': request.user,'profile': user_profile,
    }
    return render(request, 'About.html',About_Data)

from GFR_Page_Data.models import KidneyStage
from GFR_Page_Data.models import Down_Kidney_Stage
from GFR_Page_Data.models import CKDInfo
from GFR_Page_Data.models import Symptom
from GFR_Page_Data.models import RiskFactor
def eGFRCalculator(Scr, age, gender, race):
    epsilon = 1e-10  # Small value to prevent zero division
    Scr = max(Scr, epsilon)  # Ensures Scr is never zero
    if race == "black race":
        if gender == "female":
            eGFR = int(142 * min((Scr / 0.7), 1)**(-0.329) * max((Scr / 0.7), 1)**(-1.200) * (0.9938)**age * 1.012 * 1.159 + 0.5)
        elif gender == "male":
            eGFR = int(142 * min((Scr / 0.9), 1)**(-0.411) * max((Scr / 0.9), 1)**(-1.200) * (0.9938)**age * 1.159 + 0.5)
        else:
            return None
    elif race == "no black race":
        if gender == "female":
            eGFR = int(142 * min((Scr / 0.7), 1)**(-0.329) * max((Scr / 0.7), 1)**(-1.200) * (0.9938)**age * 1.012 + 0.5)
        elif gender == "male":
            eGFR = int(142 * min((Scr / 0.9), 1)**(-0.411) * max((Scr / 0.9), 1)**(-1.200) * (0.9938)**age + 0.5)
        else:
            return None
    else:
        return None
    return eGFR

def GFR(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None
        pass
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if full_name and email and message:  # Simple validation
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            return render(request,'success_page.html')  # Replace with your success URL
    ckd_info = CKDInfo.objects.first()
    symptom_data = Symptom.objects.first()
    risk_data = RiskFactor.objects.first()
    
    if request.method == "POST":
        try:
            serum_creatinine = request.POST.get("Serum_Creatinine")
            age = request.POST.get("age")
            gender = request.POST.get("gender", "").lower()
            race = request.POST.get("race", "")
            
            if not all([serum_creatinine, age, gender, race]):
                return render(request, 'eGFR_Result.html', {"result": "Invalid Input"})
            
            serum_creatinine = float(serum_creatinine)
            age = int(age)
            
            race_map = {"1": "black race", "2": "no black race"}
            race_str = race_map.get(race, "")
            
            GFR = eGFRCalculator(serum_creatinine, age, gender, race_str)
            
            kidney_stage = "Unknown"

            if GFR is not None:
                if GFR >= 90:
                    kidney_stage = "Stage 1"
                elif 60 <= GFR < 90:
                    kidney_stage = "Stage 2"
                elif 45 <= GFR < 60:
                    kidney_stage = "Stage 3a"
                elif 30 <= GFR < 45:
                    kidney_stage = "Stage 3b"
                elif 15 <= GFR < 30:
                    kidney_stage = "Stage 4"
                elif GFR < 15:
                    kidney_stage = "Stage 5"
            
            DKS = Down_Kidney_Stage.objects.all()
            kidney_stage_obj = get_object_or_404(KidneyStage, stage_name=kidney_stage)
            condition = kidney_stage_obj.Kidney_Condition if kidney_stage_obj.Kidney_Condition else ""
            bg_color = kidney_stage_obj.bg_color  # Fetch dynamic background color
            kidney_image = settings.MEDIA_URL + str(kidney_stage_obj.image) if kidney_stage_obj.image else None
            gfr_percentage = min(max((GFR / 120) * 100, 0), 100)
            
            chart_data = json.dumps([{"age": age, "gfr": round(GFR, 2)}])
            
            return render(request, 'eGFR_Result.html', {
                "result": round(GFR, 2),
                "gfr_percentage": round(gfr_percentage, 2),
                "kidney_stage_obj": kidney_stage_obj,
                "kidney_image": kidney_image,
                'DKS': DKS,
                "condition": condition,
                "chart_data": chart_data,
                "bg_color": bg_color , # Fetch color dynamically from database
                'user': request.user,
                'profile': user_profile, 
            })
        except ValueError:
            return render(request, 'eGFR_Result.html', {"result": "Invalid Input"})
    
    return render(request, 'GFR_Calculator.html', {
        'ckd_info': ckd_info,
        'symptom_data': symptom_data,
        'risk_data': risk_data,
        'user': request.user,
        'profile': user_profile,
    })

from Doctors_Data.models import Our_Doctors
from Doctors_Data.models import doctor_appointment_img
from Doctors_Data.models import Dr_Appointment
def Doctors(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None
        pass
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if full_name and email and message:  # Simple validation
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            return render(request, 'success_page.html')  # Ensure this template exists

    doctors = Our_Doctors.objects.all()  # Fetch all doctors from DB
    dr_appointment_img = doctor_appointment_img.objects.all()[:1]

    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email', None)
        location = request.POST.get('location')
        appointment_date = request.POST.get('appointment_date')

        if name and phone_number and location and appointment_date:
            # Save appointment data
            appointment = Dr_Appointment.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                location=location,
                appointment_date=appointment_date
            )

            # Send confirmation email
            send_appointment_email(email, name, appointment_date, location)

            # Redirect to confirmation page with appointment ID
            return redirect('appointment_confirmed', appointment_id=appointment.appointment_id)
        else:
            return redirect('appointment_confirmed')

    return render(request, 'Doctors.html', 
                  {
                      'doctors': doctors, 
                      'dr_appointment_img': dr_appointment_img,
                      'user': request.user,
                      'profile': user_profile,

                   })

def appointment_confirmed(request, appointment_id):
    appointment = get_object_or_404(Dr_Appointment, 
                                    appointment_id=appointment_id)
    return render(request, 'Appointment_Confirmed.html', 
                  {
                      'appointment': appointment
                   })


from Blogs_Data.models import FeaturedPost
from Blogs_Data.models import BlogPost, Writer
from Blogs_Data.models import RecommendedArticle
def Blogs(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None
        pass
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if full_name and email and message:  # Simple validation
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            return render('success_page.html')  # Replace with your success URL
    posts = FeaturedPost.objects.prefetch_related('authors', 'categories').all()
    blogs = BlogPost.objects.prefetch_related("writers", "topics").all()
    # Get unique writers from all blogs
    unique_writers = Writer.objects.filter(articles__in=blogs).distinct()[:5]
    articles = RecommendedArticle.objects.prefetch_related('experts').all()
    return render(request,'Blogs.html',{
        'posts': posts,
        'blogs': blogs,
        'top_writers': unique_writers,
        'articles': articles,
        'user': request.user,
        'profile': user_profile,
        })

# Login view
def user_login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")  # Get User ID from form input
        password = request.POST.get("password")  # Get Password from form input
        
        user = authenticate(request, username=user_id, password=password)  # Authenticate user
        
        if user is not None:
            login(request, user)
            return render(request,'Login_Successful.html')
        else:
            return render(request,'LoginFaild.html')
    return render(request,'login.html')

from Profile.models import Profile  # Assuming Profile model exists
# Registration view
def user_register(request):
    if request.method == "POST":
        uid = request.POST.get("Uid")
        first_name = request.POST.get("First_Name")
        last_name = request.POST.get("Last_Name")
        gender = request.POST.get("Gender")
        dob = request.POST.get("Dob")
        email = request.POST.get("email")
        phone_number = request.POST.get("Ph_No")
        password = request.POST.get("Password")
        confirm_password = request.POST.get("Confirm_Password")

        # Validation
        if password != confirm_password:
            return redirect("register")

        if User.objects.filter(username=uid).exists():
            return render(request,'ExistingUid.html')

        if User.objects.filter(email=email).exists():
            return render(request,'ExistingEmail.html')

        # Creating the user and profile
        user = User.objects.create(
            username=uid, 
            first_name=first_name, 
            last_name=last_name, 
            email=email,
            password=make_password(password)  # Hashing password for security
        )
        
        profile = Profile.objects.create(
            Name=f"{first_name} {last_name}",
            Gender=gender,
            dob=dob,
            Phone_Number=phone_number,
            email=email,
            user=user  # If `Profile` has a foreign key to `User`
        )
        return render(request,'Registration_Successful.html')
    return render(request, 'registration.html') # Ensure this template corresponds to your registration page

# Logout view
def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')  # Redirects to the home page

def Header(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None
    return render(request, 'header.html', {
        'user': request.user,
        'profile': user_profile,  # Pass profile picture URL
    })
def Footer(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if full_name and email and message:  # Simple validation
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            return render('success_page.html')  # Replace with your success URL
    return render(request, 'footer.html')

# Render chatbot page with previous chat history
from ChatBot_Data.models import ChatbotSuggestion, ChatResponse
@login_required(login_url='login')
def chatbot_page(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None
        pass
    Question_suggestions = ChatbotSuggestion.objects.all()[:5]  # Limit to 5 suggestions
    chat_history = request.session.get("chat_history", [])
    return render(request, "ChatBot.html", {
        "chat_history": chat_history,
        'Question_suggestions': Question_suggestions,
        'user': request.user,
        'profile': user_profile,
    })

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip().lower()

            # Fetch response from database (enhanced with fuzzy matching)
            response_entry = ChatResponse.objects.filter(Q(question__iexact=user_message) | Q(question__icontains=user_message)).first()
            bot_response = response_entry.answer if response_entry else "I'm not sure, but I specialize in kidney health!"

            # Get current time
            current_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")

            # Manage chat history (increase limit to 50 messages)
            chat_history = deque(request.session.get("chat_history", []), maxlen=50)
            chat_history.append({"text": user_message, "sender": "user", "time": current_time})
            chat_history.append({"text": bot_response, "sender": "bot", "time": current_time})

            request.session["chat_history"] = list(chat_history)
            request.session.modified = True

            return JsonResponse({"response": bot_response})

        except json.JSONDecodeError:
            return JsonResponse({"response": "Invalid JSON format"}, status=400)

    return JsonResponse({"response": "Invalid request"}, status=400)

@csrf_exempt
def autocomplete_suggestions(request):
    if request.method == "GET":
        query = request.GET.get("q", "").strip()
        suggestions = []

        if query:
            suggestions = ChatResponse.objects.filter(Q(question__istartswith=query)).values_list("question", flat=True)[:5]

        return JsonResponse({"suggestions": list(suggestions)})

    return JsonResponse({"error": "Invalid request"}, status=400)

from Terms_Conditions_And_privacy_policy.models import TermsAndConditions
def terms_conditions(request):
    terms = TermsAndConditions.objects.all()
    return render(request,'terms_conditions.html',{'terms': terms})

from Terms_Conditions_And_privacy_policy.models import PrivacyPolicy
def privacy_policy(request):
    policies = PrivacyPolicy.objects.all()
    return render(request,'privacy_policy.html',{"policies": policies})

token_generator = PasswordResetTokenGenerator()

def send_password_reset_email(email, reset_link):
    subject = "🔐 Reset Your Password - YourWebsite"
    html_message = render_to_string("password_reset_email.html", {"reset_link": reset_link})
    plain_message = strip_tags(html_message)  # Converts HTML to plain text as a fallback

    send_mail(
        subject,
        plain_message,
        "noreply@yourwebsite.com",
        [email],
        html_message=html_message,
        fail_silently=False,
    )

def send_appointment_email(email, name, appointment_date, location):
    if email:  # Only send email if provided
        subject = "✅ Your Appointment Confirmation"
        html_message = render_to_string("appointment_confirmation.html", {
            "name": name,
            "appointment_date": appointment_date,
            "location": location
        })
        plain_message = strip_tags(html_message)  # Convert HTML to plain text fallback

        send_mail(
            subject,
            plain_message,
            "noreply@yourwebsite.com",
            [email],
            html_message=html_message,
            fail_silently=False,
        )

def password_reset_request(request: HttpRequest):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            # Get the current site domain
            current_site = request.get_host()
            reset_link = f"http://{current_site}/reset-password/{uid}/{token}/"

            # Send email with password reset link
            send_password_reset_email(email, reset_link)

            return render(request, "password_reset_done.html")

        except User.DoesNotExist:
            return render(request, "password_reset.html", {"error": "Email not found"})

    return render(request, "password_reset.html")

def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if token_generator.check_token(user, token):  # Check if token is valid
            if request.method == "POST":
                new_password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')

                if new_password == confirm_password:
                    user.password = make_password(new_password)  # Hash the password
                    user.save()
                    return redirect("password_reset_complete")
                else:
                    return render(request, "reset_password.html", {"error": "Passwords do not match"})

            return render(request, "reset_password.html")

        else:
            return render(request, "reset_password.html", {"error": "Invalid or expired link"})

    except (TypeError, ValueError, User.DoesNotExist):
        return render(request, "reset_password.html", {"error": "Invalid link"})
    
def password_reset_complete(request):
    return render(request, "password_reset_complete.html")

@login_required
def add_profile_picture(request):
    user_profile = Profile.objects.get(user=request.user)
    user_profile, created = Profile.objects.get_or_create(user=request.user)  # Get profile for logged-in user

    if request.method == 'POST' and 'profile_picture' in request.FILES:
        user_profile.profile_picture = request.FILES['profile_picture']
        user_profile.save()
        return redirect('home')  # Redirect to profile page (update with your actual profile URL name)

    return render(request, 'add_profile_picture.html', {'profile': user_profile})

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "profile_view.html", {"profile": profile})

# Define file paths
csv_path = os.path.join(settings.BASE_DIR, "Data/kidney_data.csv")
models_dir = os.path.join(settings.BASE_DIR, "models")
model_path = os.path.join(models_dir, "kidney_model.pkl")
encoder_path = os.path.join(models_dir, "label_encoders.pkl")

# Ensure models directory exists
os.makedirs(models_dir, exist_ok=True)

# Define feature columns
FEATURE_COLUMNS = [
    "Kidney Cysts (count)", "Age", "Gender", "Diabetes", "Genetics", 
    "Kidney Size (cm)", "Blood Pressure (mmHg)", "Creatinine Level (mg/dL)"
]

def train_model():
    """Train the model if missing and save it."""
    if not os.path.exists(csv_path):
        print("Dataset not found!")
        return False

    df = pd.read_csv(csv_path)
    
    # Encode categorical variables
    label_encoders = {}
    for col in ["Gender", "Diabetes", "Genetics"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    joblib.dump(label_encoders, encoder_path)
    
    X = df.drop(columns=["Kidney Failure (%)"])
    y = df["Kidney Failure (%)"]
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    joblib.dump(model, model_path)
    print("Model training complete!")
    return True

from ADPKD_Data.models import SeverityStage, ManagementStage
def get_adpkd_stage(mutation_type, age, egfr):
    age_ranges = {
        "pkd1": [(0, 24, "Stage-1"), (25, 44, "Stage-2"), 
                 (45, 54, "Stage-3"), (55, 64, "Stage-4"), 
                 (65, float("inf"), "Stage-5")],
        "pkd2": [(0, 34, "Stage-1"), (35, 54, "Stage-2"), 
                 (55, 64, "Stage-3"), (65, 74, "Stage-4"), 
                 (75, float("inf"), "Stage-5")],
    }

    if mutation_type in age_ranges:
        for min_age, max_age, stage_number in age_ranges[mutation_type]:
            if min_age <= age <= max_age:
                stage = SeverityStage.objects.filter(stage_number=stage_number).first()
                if stage:
                    return {
                        "stage": stage.stage_number,
                        "heading": stage.stage_heading,
                        "title": stage.stage_title,
                        "color": stage.stage_color,
                        "image": stage.stage_image.url if stage.stage_image else None,
                        "egfr_status": "Normal" if egfr >= 90 else "Low"
                    }

    return None

def calculate_adpkd_risk(cysts, age, family_history, kidney_size, systolic_bp, serum_creatinine):
    """Calculate ADPKD risk based on input parameters."""
    risk = 0

    #  Number of Cysts
    if cysts >= 40:
        risk += 35
    elif cysts >= 20:
        risk += 30
    elif cysts >= 10:
        risk += 20
    elif cysts >= 5:
        risk += 10
    elif cysts == 0 and family_history.lower() == "yes":
        risk += 5  # If no cysts, only family history increases risk

    # Age Factor
    if age >= 70:
        risk += 25
    elif age >= 60:
        risk += 22
    elif age >= 50:
        risk += 18
    elif age >= 40:
        risk += 15
    elif age >= 30:
        risk += 12
    elif age >= 20:
        risk += 10
    elif age >= 10:
        risk += 7
    elif age >= 5:
        risk += 5

    # Family History
    if family_history.lower() == "yes":
        risk += 30

    #  Kidney Size
    if kidney_size >= 18:
        risk += 30
    elif kidney_size >= 16:
        risk += 25
    elif kidney_size >= 14:
        risk += 20
    elif kidney_size >= 12:
        risk += 15
    elif kidney_size >= 10:
        risk += 10

    #  Systolic Blood Pressure
    if systolic_bp >= 160:
        risk += 20
    elif systolic_bp >= 140:
        risk += 15
    elif systolic_bp >= 130:
        risk += 10

    #  Serum Creatinine
    if serum_creatinine >= 2.5:
        risk += 30
    elif serum_creatinine >= 2.0:
        risk += 25
    elif serum_creatinine >= 1.5:
        risk += 20
    elif serum_creatinine >= 1.2:
        risk += 15
    elif serum_creatinine >= 1.0:
        risk += 10

    # Ensure risk does not exceed 100%
    return min(risk, 100)

def calculate_bp_percentage(age, gender, measured_sbp):
    """Calculate BP status and normal BP based on age and gender."""
    
    # Define normal SBP based on age and gender
    if 5 <= age < 10:
        normal_sbp = 95 if gender.lower() == "male" else 90
    elif 10 <= age < 20:
        normal_sbp = 105 if gender.lower() == "male" else 100
    elif 20 <= age < 30:
        normal_sbp = 115 if gender.lower() == "male" else 110
    elif 30 <= age < 40:
        normal_sbp = 120 if gender.lower() == "male" else 115
    elif 40 <= age < 50:
        normal_sbp = 125 if gender.lower() == "male" else 120
    elif 50 <= age < 60:
        normal_sbp = 130 if gender.lower() == "male" else 125
    elif age >= 60:
        normal_sbp = 135 if gender.lower() == "male" else 130
    else:
        return "Invalid age", None

    # Calculate BP percentage deviation
    bp_percentage = ((measured_sbp - normal_sbp) / normal_sbp) * 100

    # Determine BP status
    if bp_percentage > 0:
        return f"{bp_percentage:.2f}", int(normal_sbp)
    elif bp_percentage < 0:
       return f"{abs(bp_percentage):.2f}", int(normal_sbp)
    else:
        return "0.00%", int(normal_sbp)

def CKFPercentage(eGFR):
    normal_eGFR = 90  # Normal eGFR value (mL/min/1.73m²)

    if eGFR <= 0:
        return None  # Return None instead of "Invalid" to handle it better in the template

    if eGFR >= normal_eGFR:
        return 100  # Return integer value instead of a string

    # Calculate kidney function percentage
    kidney_function_percentage = (eGFR / normal_eGFR) * 100
    return round(kidney_function_percentage, 2)  # Return float instead of string

def kidney_function_chart(age, predicted_data, genetics):
    """Generate kidney function prediction data based on provided parameters."""
    try:
        age = int(age)
        kidney_function_percentage = float(predicted_data)  # Using predicted_data as initial function percentage
    except ValueError:
        age = 40
        kidney_function_percentage = 90

    # Set logistic function parameters based on genetics type
    if genetics == "PKD1":
        L, x0, k = 100, 50, 0.15  # PKD1 Growth Parameters
    else:
        L, x0, k = 100, 60, 0.10  # PKD2 Growth Parameters

    # Logistic function to predict failure rate
    def logistic(x):
        return L / (1 + np.exp(-k * (x - x0)))

    # Generate data for the next 20 years
    labels = list(range(age, age + 21))
    dataPoints = [kidney_function_percentage] + [logistic(a) for a in range(age + 1, age + 21)]
    return {"labels": labels, "dataPoints": dataPoints}

@login_required(login_url='login')
def ADPKD(request):
    user_profile = None  # Default value
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile does not exist
    else:
        user_profile = None

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if full_name and email and message:  # Simple validation
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            return render(request,'success_page.html')
    """Predict ADPKD stage using a trained model."""
    if not os.path.exists(model_path) or not os.path.exists(encoder_path):
        train_model()
    
    try:
        model = joblib.load(model_path)
        label_encoders = joblib.load(encoder_path)
    except Exception as e:
        return render(request, "ADPKD.html")

    if request.method == "POST":
        try:
            cysts = int(request.POST.get("cysts", 0) or 0)
            age = int(request.POST.get("age", 0) or 0)
            gender = request.POST.get("gen", "Male")
            diabetes = request.POST.get("Diabetes", "No")
            genetics = request.POST.get("geneticADPKD", "pkd1")
            kidney_size = float(request.POST.get("kidney_size", 0) or 0)
            blood_pressure = float(request.POST.get("blood_pressure", 0) or 0)
            serum_creatinine = float(request.POST.get("serum_creatinine", 0) or 0)
            Family_History = request.POST.get('famHistADPKD')
            GFR_Value = int(request.POST.get('gfr', 0) or 0)

            Input_gender=gender
            Input_genetics=genetics

            def safe_encode(label, encoder, default=0):
                return encoder.transform([label])[0] if label in encoder.classes_ else default

            gender = safe_encode(gender, label_encoders["Gender"])
            diabetes = safe_encode(diabetes, label_encoders["Diabetes"])
            genetics = safe_encode(genetics, label_encoders["Genetics"])

            feature_data = pd.DataFrame([[cysts, age, gender, diabetes, genetics, kidney_size, blood_pressure, serum_creatinine]],
                                        columns=FEATURE_COLUMNS)
            feature_data = feature_data[model.feature_names_in_]
            predicted_data = model.predict(feature_data)[0]

            stage_info = get_adpkd_stage(request.POST.get("geneticADPKD",
                                                           "pkd1"), age, GFR_Value)
            adpkd_risk = calculate_adpkd_risk(cysts, age, Family_History, 
                                              kidney_size, blood_pressure, serum_creatinine)
            # Calculate BP Status
            bp_status, normal_bp = calculate_bp_percentage(age, Input_gender,
                                                            blood_pressure)
            kidney_function_percentage = CKFPercentage(GFR_Value)
            graph_data = kidney_function_chart(age, predicted_data,
                                                Input_genetics)
            graph_json = json.dumps(graph_data)  # Convert to JSON
        
            stages = ManagementStage.objects.all()[:5]

            context = {
                "stage": stage_info,
                "serum_creatinine": serum_creatinine,
                "kidney_size": kidney_size,
                "genetics": genetics,
                "predicted_data": round(predicted_data, 2),
                "GFR_Value": GFR_Value,
                "age": age,
                "cysts": cysts,
                "Family_History": Family_History,
                "gender": Input_gender.capitalize(),
                "stages": stages,
                "Input_genetics":Input_genetics,
                "ADPKD_Risk": adpkd_risk,
                "blood_pressure": blood_pressure,
                "BP_Status": bp_status,
                "Normal_BP": normal_bp,
                "kidney_function_percentage": kidney_function_percentage,
                "graph_data": graph_json,  # Pass as JSON
                'user': request.user,
                'profile': user_profile,
            }

            if stage_info:
                return render(request, "ADPKD_Result.html", context)
            else:
                return redirect("ADPKD")  

        except Exception:
            return render(request, "ADPKD.html")

    return render(request, "ADPKD.html",
                  {
                      'user': request.user,''
                      'profile': user_profile
    })