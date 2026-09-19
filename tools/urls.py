from django.urls import path, include
from . import views
from .views import HomeView, AppointmentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('appointment/<int:pk>', AppointmentView.as_view(), name='appointment'),
    path('appointment_detail/<int:pk>', AppointmentView.as_view(), name='appointment_detail'),
    path('add_appointment/', AppointmentView.as_view(), name='add_appointment'),
]