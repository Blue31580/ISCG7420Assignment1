from django.contrib import admin

from tools.models import Appointment, Profile, Specialization, Appointment_Slot

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Profile)
admin.site.register(Specialization)
admin.site.register(Appointment_Slot)