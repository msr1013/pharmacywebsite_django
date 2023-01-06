from django.urls import path
from . import views

urlpatterns = [
    path('medicines/', views.medicine_index, name='medicines'),
]
