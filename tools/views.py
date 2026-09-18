from django.shortcuts import render
from django.views.generic import ListView, CreateView

from tools.models import Appointment


# Create your views here.
class HomeView(ListView):
    model = Appointment
    template_name = 'home.html'

class AppointmentView(ListView):
    model = Appointment
    template_name = 'appointment.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = 'appointment_create.html'
    fields = ['appointment_details', 'appointment_status']
