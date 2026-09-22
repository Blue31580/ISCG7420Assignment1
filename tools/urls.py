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
]