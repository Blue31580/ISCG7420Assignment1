from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from tools.forms import AppointmentForm, DoctorForm, DoctorSlotForm
from tools.models import Appointment, Doctor, Appointment_Slot


# Create your views here.
class HomeView(ListView):
    model = Doctor
    template_name = 'home.html'


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


# ----- Staff dashboard (Doctor profile management + all appointments) -----

def is_staff_user(user):
    return user.is_authenticated and user.is_staff


staff_required = user_passes_test(is_staff_user, login_url='login')


@staff_required
def dashboard_home(request):
    context = {
        'doctor_count': Doctor.objects.count(),
        'slot_count': Appointment_Slot.objects.count(),
        'appointment_count': Appointment.objects.count(),
    }
    return render(request, 'dashboard/home.html', context)


@staff_required
def dashboard_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'dashboard/doctors.html', {'doctors': doctors})


@staff_required
def dashboard_doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_doctors')
    else:
        form = DoctorForm()
    return render(request, 'dashboard/doctor_form.html', {'form': form})


@staff_required
def dashboard_doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('dashboard_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'dashboard/doctor_form.html', {'form': form, 'doctor': doctor})


@staff_required
def dashboard_doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('dashboard_doctors')
    return render(request, 'dashboard/doctor_delete.html', {'doctor': doctor})


@staff_required
def dashboard_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'dashboard/appointments.html', {'appointments': appointments})


@staff_required
def dashboard_appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.slot.is_booked = False
        appointment.slot.save()
        appointment.delete()
        return redirect('dashboard_appointments')
    return render(request, 'dashboard/appointment_delete.html', {'appointment': appointment})


# ----- Doctor self-service (their own slots + appointments) -----

def is_doctor_user(user):
    return user.is_authenticated and hasattr(user, 'doctor_profile')


doctor_required = user_passes_test(is_doctor_user, login_url='login')


@doctor_required
def doctor_dashboard(request):
    doctor = request.user.doctor_profile
    slots = doctor.slots.all()
    return render(request, 'doctor_slots/slots.html', {'doctor': doctor, 'slots': slots})


@doctor_required
def doctor_slot_add(request):
    doctor = request.user.doctor_profile
    if request.method == 'POST':
        form = DoctorSlotForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.doctor = doctor
            slot.save()
            return redirect('doctor_dashboard')
    else:
        form = DoctorSlotForm()
    return render(request, 'doctor_slots/slot_form.html', {'form': form})


@doctor_required
def doctor_slot_edit(request, pk):
    doctor = request.user.doctor_profile
    slot = get_object_or_404(Appointment_Slot, pk=pk, doctor=doctor)
    if request.method == 'POST':
        form = DoctorSlotForm(request.POST, instance=slot)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = DoctorSlotForm(instance=slot)
    return render(request, 'doctor_slots/slot_form.html', {'form': form, 'slot': slot})


@doctor_required
def doctor_slot_delete(request, pk):
    doctor = request.user.doctor_profile
    slot = get_object_or_404(Appointment_Slot, pk=pk, doctor=doctor)
    if request.method == 'POST':
        slot.delete()
        return redirect('doctor_dashboard')
    return render(request, 'doctor_slots/slot_delete.html', {'slot': slot})


@doctor_required
def doctor_appointments(request):
    doctor = request.user.doctor_profile
    appointments = Appointment.objects.filter(slot__doctor=doctor)
    return render(request, 'doctor_slots/appointments.html', {'appointments': appointments})