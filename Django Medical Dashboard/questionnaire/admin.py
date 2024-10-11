from django.contrib import admin
from .models import Questionnaire, PatientResponse, Attempt

# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(PatientResponse)
admin.site.register(Attempt)