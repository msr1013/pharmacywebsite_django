from rest_framework import serializers
from medicines.models import Medicine, Category


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "description", "expiry_date",
                  "mg", "price", "quantity", "category")
        model = Medicine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("Catrogory")
        model = Category
