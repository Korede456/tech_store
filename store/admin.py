from django.contrib import admin
from .models import Laptop

class LaptopAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "processor", "ram", "storage_capacity", "price", "available")
    list_filter = ("brand", "processor", "ram", "condition", "available")
    search_fields = ("brand", "model", "processor", "ram")
    ordering = ("brand", "model")

admin.site.register(Laptop, LaptopAdmin)
