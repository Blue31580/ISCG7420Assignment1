from django.contrib import admin

from tools.models import Appointment, Specialization, Appointment_Slot

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Specialization)
admin.site.register(Appointment_Slot)