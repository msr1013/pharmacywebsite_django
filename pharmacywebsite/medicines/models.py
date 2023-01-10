from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        db_table = "app_categories"


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    expiry_date = models.DateTimeField()
    mg = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()
    entry_date = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "app_medicines"
