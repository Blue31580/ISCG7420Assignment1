from django.urls import path, include
from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('register_form', views.register_view, name='register_form'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:doctor_id>/slots/', views.doctor_slots, name='doctor_slots'),
    path('slots/<int:slot_id>/book/', views.book_slot, name='book_slot'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('my_appointments/<int:pk>/cancel/', views.cancel_appointment, name='cancel_appointment'),

    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/doctors/', views.dashboard_doctors, name='dashboard_doctors'),
    path('dashboard/doctors/add/', views.dashboard_doctor_add, name='dashboard_doctor_add'),
    path('dashboard/doctors/<int:pk>/edit/', views.dashboard_doctor_edit, name='dashboard_doctor_edit'),
    path('dashboard/doctors/<int:pk>/delete/', views.dashboard_doctor_delete, name='dashboard_doctor_delete'),
    path('dashboard/appointments/', views.dashboard_appointments, name='dashboard_appointments'),
    path('dashboard/appointments/<int:pk>/cancel/', views.dashboard_appointment_cancel, name='dashboard_appointment_cancel'),

    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/slots/add/', views.doctor_slot_add, name='doctor_slot_add'),
    path('doctor/slots/<int:pk>/edit/', views.doctor_slot_edit, name='doctor_slot_edit'),
    path('doctor/slots/<int:pk>/delete/', views.doctor_slot_delete, name='doctor_slot_delete'),
    path('doctor/appointments/', views.doctor_appointments, name='doctor_appointments'),

]