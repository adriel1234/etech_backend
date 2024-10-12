from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from teste import models, serializers, filters


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filterset_class = filters.ClientFilter
    permission_classes = {permissions.IsAuthenticated}

    @action(detail=False, methods=['GET'])
    def teste(self, request, *args, **kwargs):
        return Response({'teste': 1}, status=200)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    permission_classes = {permissions.IsAuthenticated}

    @action(detail=False, methods=['GET'])
    def product_teste(self, request, *args, **kwargs):
        # products = self.queryset.all().values('description', 'quantity')
        # products = self.queryset.all()
        products = self.queryset.get(id=1)
        p_serializer = self.get_serializer(products)

        return Response(p_serializer.data, status=200)


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
