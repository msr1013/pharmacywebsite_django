from django.contrib import admin
from medicines.models import Medicine, Category


# Register your models here.

class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "expiry_date",
                    "mg", "price", "quantity", "category")
    search_fields = ("name",)
    list_filter = ("name", "category",)


admin.site.register(Category)
admin.site.register(Medicine, MedicineAdmin)

admin.site.site_header = "Admin Panel"
admin.site.index_title = "Pharmacy"
admin.site.site_title = "Admin Panel"
