from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from tools.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_details']

        widgets = {
            'appointment_details': forms.Textarea(attrs={'class': 'form-control'}),
        }