from django.urls import path, include
from . import views
from .views import HomeView, AppointmentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('appointment/<int:pk>', AppointmentView.as_view(), name='appointment'),
]