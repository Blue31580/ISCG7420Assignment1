from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from tools.models import Appointment, Doctor, Appointment_Slot


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_details']

        widgets = {
            'appointment_details': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user', 'specialization', 'room_number', 'bio', 'profile_pic', 'consultation_fee']

class DoctorSlotForm(forms.ModelForm):
    class Meta:
        model = Appointment_Slot
        fields = ['appointment_date', 'appointment_time', 'appointment_end_time']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
            'appointment_end_time': forms.TimeInput(attrs={'type': 'time'}),
        }