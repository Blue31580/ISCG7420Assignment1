from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def name(self):
        return self.user.get_full_name() or self.user.username

    def __str__(self):
        return self.name

class Appointment_Slot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='slots')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor', 'appointment_date', 'appointment_time')
        ordering = ['appointment_date', 'appointment_time']

    def __str__(self):
       return f"{self.doctor.name} - {self.appointment_date} {self.appointment_time}"

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    slot = models.OneToOneField(Appointment_Slot, on_delete=models.CASCADE, related_name='appointment')
    appointment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    appointment_details = models.TextField(blank=True)
    appointment_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} - {self.slot} ({self.appointment_status})"




