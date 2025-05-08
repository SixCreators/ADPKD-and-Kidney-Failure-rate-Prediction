from django.contrib import admin
from GFR_Page_Data.models import KidneyStage
from GFR_Page_Data.models import Down_Kidney_Stage
admin.site.register(KidneyStage)
admin.site.register(Down_Kidney_Stage)
from GFR_Page_Data.models import CKDInfo
admin.site.register(CKDInfo)
from GFR_Page_Data.models import Symptom
admin.site.register(Symptom)
from GFR_Page_Data.models import RiskFactor
admin.site.register(RiskFactor)
# Register your models here.
