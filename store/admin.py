from django.contrib import admin
from .models import Laptop
from .models import Cart, CartItem
from .models import Order, OrderItem


class LaptopAdmin(admin.ModelAdmin):
    list_display = (
        "brand",
        "model",
        "processor",
        "ram",
        "storage_capacity",
        "price",
        "available",
    )
    list_filter = ("brand", "processor", "ram", "condition", "available")
    search_fields = ("brand", "model", "processor", "ram")
    ordering = ("brand", "model")


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user__email",)
    ordering = ("created_at",)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "laptop", "quantity", "total_price")
    search_fields = ("cart__user__email", "laptop__brand", "laptop__model")
    ordering = ("cart", "laptop")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_price", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("user__email", "status")
    ordering = ("-created_at",)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "laptop", "quantity", "price")
    search_fields = ("order__user__email", "laptop__brand", "laptop__model")
    ordering = ("order", "laptop")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Laptop, LaptopAdmin)
