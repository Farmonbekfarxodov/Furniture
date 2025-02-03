from django.contrib import admin
from .models import OrderModel, OrderItem


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'total_product', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')  # Assuming UserModel has 'username' and 'email' fields
    ordering = ('-created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order__id', 'product', 'product_name', 'product_price', 'quantity', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('product_name', 'order__user__username', 'order__user__email')  # Assuming related fields
    ordering = ('-created_at',)
