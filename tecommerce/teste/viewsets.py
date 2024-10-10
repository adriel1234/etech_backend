from rest_framework import viewsets, permissions
from teste import models, serializers, filters


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filterset_class = filters.ClientFilter
    permission_classes = {permissions.IsAuthenticated}


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    permission_classes = {permissions.IsAuthenticated}


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filterset_class = filters.EmployeeFilter
    permission_classes = {permissions.IsAuthenticated}


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    filterset_class = filters.SaleFilter
    permission_classes = {permissions.IsAuthenticated}
