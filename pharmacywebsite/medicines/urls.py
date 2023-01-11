from django.urls import path
from . import views

urlpatterns = [
    path('medicines/', views.medicine_index, name='medicines'),
    path('add-medicine/', views.medicine_create, name='add-medicine'),

    # categories
    path('add-category/', views.category_create, name='add-category'),
]
