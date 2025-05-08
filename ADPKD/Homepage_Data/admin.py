from django.contrib import admin
from Homepage_Data.models import Kidney_Anatomy
from Homepage_Data.models import kidney_blood_flow
from Homepage_Data.models import HKVSDK
from Homepage_Data.models import CKD
from Homepage_Data.models import PKD
from Homepage_Data.models import slider_section
from Homepage_Data.models import Reference
from Homepage_Data.models import home_top_content
from Homepage_Data.models import home_top_img
from Homepage_Data.models import card_section
admin.site.register(Kidney_Anatomy)
admin.site.register(kidney_blood_flow)
admin.site.register(HKVSDK)
admin.site.register(CKD)
admin.site.register(PKD)
admin.site.register(slider_section)
admin.site.register(Reference)
admin.site.register(home_top_content)
admin.site.register(home_top_img)
admin.site.register(card_section)

# Register your models here.
