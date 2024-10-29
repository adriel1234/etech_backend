from rest_framework import serializers
from core import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        exclude = ['created_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        # exclude = ['created_at']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        exclude = ['created_at']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sale
        exclude = ['created_at']
