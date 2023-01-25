from rest_framework import serializers
from medicines.models import Medicine, Category


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "description", "expiry_date",
                  "mg", "price", "quantity", "category", "user")
        model = Medicine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("Category")
        model = Category
