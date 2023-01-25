from django.urls import path
from medicineapi.views import MedicineApiView, MedicineApiIdView

urlpatterns = [
    path('medicine/', MedicineApiView.as_view()),
    path('medicine/<int:id>', MedicineApiIdView.as_view())
]
