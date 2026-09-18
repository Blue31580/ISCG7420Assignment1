from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Appointment(models.Model):
    #patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now_add=True)
    appointment_time = models.TimeField(auto_now_add=True)
    appointment_status = models.CharField(max_length=20, default='pending')
    appointment_details = models.TextField()

    def __str__(self):
        return self.appointment_details + " - " + self.appointment_status

    def get_absolute_url(self):
        #return reverse('appointment', kwargs={'pk': self.pk})
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

class Specialization(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.specialization

class Appointment_Slot(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now_add=True)
    appointment_time = models.TimeField(auto_now_add=True)
    appointment_end_time = models.TimeField(auto_now_add=True)
    appointment_status = models.CharField(max_length=20, default='pending')
    active = models.BooleanField(default=True)
    appointment_details = models.TextField()

    def __str__(self):
       return self.doctor.username + " - " + self.appointment_status


