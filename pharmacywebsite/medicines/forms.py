from django import forms
from medicines.models import Medicine, Category


class MedicineCreateForm(forms.ModelForm):
    class Meta:
        fields = ("name", "description", "expiry_date",
                  "mg", "price", "quantity", "category")
        model = Medicine


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        fields = ("category",)
        model = Category
