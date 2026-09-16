from django.db import models

# Create your models here.
class Appointment(models.Model):
    #patient = models.ForeignKey(User, on_delete=models.CASCADE)
    #doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now_add=True)
    appointment_time = models.TimeField(auto_now_add=True)
    appointment_status = models.CharField(max_length=20, default='pending')
    appointment_details = models.TextField()

    def __str__(self):
        return self.appointment_details + " - " + self.appointment_status