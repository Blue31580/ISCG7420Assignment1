from django.shortcuts import render
from django.views.generic import ListView

from tools.models import Appointment


# Create your views here.
class HomeView(ListView):
    model = Appointment
    template_name = 'home.html'

class AppointmentView(ListView):
    model = Appointment
    template_name = 'appointment.html'
