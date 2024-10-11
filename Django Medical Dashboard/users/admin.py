from .models import User, PatientProfile, DoctorProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

class UserAdminClass(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('is_patient', 'is_doctor', 'phone_number', 'date_of_birth', 'address', 'emergency_contact')}),
    )
    # fields = ["is_patient", "is_doctor", "phone_number", "date_of_birth", "address", "emergency_contact"]

admin.site.register(User, UserAdminClass)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)