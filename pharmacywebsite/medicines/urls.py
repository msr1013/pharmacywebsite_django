from django.urls import path
from . import views

urlpatterns = [
    path('medicines/', views.medicine_index, name='medicines'),
    path('add-medicine/', views.medicine_create, name='add-medicine'),
    path('update-medicine/', views.medicine_update, name='update-medicine'),
    path('edit_medicine/<int:id>', views.medicine_edit, name='edit-medicine'),
    path('show_medicine/<int:id>', views.medicine_show, name='show-medicine'),
    path('delete_medicine/<int:id>', views.medicine_delete, name='delete-medicine'),

    # categories
    path('add-category/', views.category_create, name='add-category'),
]
