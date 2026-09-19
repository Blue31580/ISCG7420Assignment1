from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

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

class AppointmentView(ListView):
    model = Appointment
    template_name = 'appointment.html'
    context_object_name = 'appointments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

def appointment_detail(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    return render(request, 'appointment_detail.html', {'appointment': appointment})