from django.contrib import admin
from .models import AppOrder


@admin.register(AppOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'size',
        'order_status',
        'quantity',
        'created_at',
        'updated_at'
        ]
    
    list_filter = [
        'created_at',
        'order_status',
        'size',
    ]