from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView

from tools.forms import AppointmentForm
from tools.models import Appointment, Doctor, Appointment_Slot


# Create your views here.
class HomeView(ListView):
    model = Doctor
    template_name = 'home.html'

#class AppointmentCreateView(CreateView):
 #   model = Appointment
 #   template_name = 'appointment_create.html'
 #  fields = ['appointment_details', 'appointment_status']

#class AppointmentView(ListView):
 #   model = Appointment
  #  template_name = 'appointment.html'
   # context_object_name = 'appointments'

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  context['users'] = User.objects.all()
       # return context

#class AppointmentCreateView(CreateView):
 #   model = Appointment
  #  template_name = 'appointment_create.html'
   # fields = ['doctor','appointment_details', 'appointment_status']

#def appointment_detail(request, pk):
 #   appointment = Appointment.objects.get(pk=pk)
  #  return render(request, 'appointment_detail.html', {'appointment': appointment})

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username=username, email=email)
    user.set_password(password)
    user.save()
    return redirect('login')

def register_view(request):
    return render(request, 'register.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_slots(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    slots = doctor.slots.filter(is_booked=False)
    return render(request, 'doctor_slots.html', {'doctor': doctor, 'slots': slots})

@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(Appointment_Slot, pk=slot_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.slot = slot
            appointment.save()
            slot.is_booked = True
            slot.save()
            return redirect('my_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'book_slot.html', {'slot': slot, 'form': form})

@login_required
def my_appointments(request):
    appointments = request.user.appointments.all()
    return render(request, 'my_appointments.html', {'appointments': appointments})

@login_required
def cancel_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient=request.user)

    if request.method == 'POST':
        appointment.slot.is_booked = False
        appointment.slot.save()
        appointment.delete()
        return redirect('my_appointments')

    return render(request, 'cancel_appointment.html', {'appointment': appointment})
