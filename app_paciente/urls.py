from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_live_side, name='inicio_live_side'),
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('ver_pacientes/', views.ver_pacientes, name='ver_pacientes'),
    path('actualizar_paciente/<int:id>/', views.actualizar_paciente, name='actualizar_paciente'),
    path('realizar_actualizacion_paciente/<int:id>/', views.realizar_actualizacion_paciente, name='realizar_actualizacion_paciente'),
    path('borrar_paciente/<int:id>/', views.borrar_paciente, name='borrar_paciente'),
]
