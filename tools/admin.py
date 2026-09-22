from django.contrib import admin

from tools.models import Doctor, Appointment, Appointment_Slot

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appointment_Slot)
admin.site.register(Appointment)