from rest_framework import serializers
from .models import AppOrder


class AppOrderSeraializer(serializers.ModelSerializer):
    class Meta:
        model = AppOrder
        fields = [
            'size', 
            'order_status', 
            'quantity'
        ]