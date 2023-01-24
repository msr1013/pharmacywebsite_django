from django.urls import path
from medicineapi.views import MedicineApiView

urlpatterns = [
    path('medicine/', MedicineApiView.as_view()),
]
