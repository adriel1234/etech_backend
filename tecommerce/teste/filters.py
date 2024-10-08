from django_filters import rest_framework as filters

from teste import models

# Filtro de pesquisa
LIKE = 'unaccent__icontains'
EQUALS = 'exact'
STARTS_WITH = 'startswith'
GT = 'gt'
GTE = 'gte'
LT = 'lt'
LTE = 'lte'
IN = 'in'


class ClientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    cpf_sw = filters.CharFilter(field_name='cpf', lookup_expr=STARTS_WITH)
    cpf_equals = filters.CharFilter(field_name='cpf', lookup_expr=EQUALS)
    rg = filters.CharFilter(lookup_expr=STARTS_WITH)
    age = filters.NumberFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Client
        fields = ['nome', 'cpf_sw', 'cpf_equals', 'rg', 'age']


class ProductFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr=LIKE)
    quantity_equals = filters.NumberFilter(field_name='quantity', lookup_expr=EQUALS)
    quantity_gt = filters.NumberFilter(field_name='quantity', lookup_expr=GT)

    class Meta:
        model = models.Product
        fields = ['description', 'quantity_equals', 'quantity_gt']


class EmployeeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    registration = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Employee
        fields = ['name', 'registration']


class SaleFilter(filters.FilterSet):
    nrf = filters.CharFilter(lookup_expr=LIKE)
    product = filters.CharFilter(field_name='product__description', lookup_expr=LIKE)
    client = filters.CharFilter(field_name='client__name', lookup_expr=LIKE)
    cpf_client = filters.CharFilter(field_name='client__cpf', lookup_expr=STARTS_WITH)
    employee = filters.CharFilter(field_name='employee__description', lookup_expr=LIKE)
    registration_employee = filters.CharFilter(field_name='employee__registration', lookup_expr=LIKE)

    class Meta:
        model = models.Sale
        fields = ['nrf', 'product', 'client', 'employee', 'registration_employee', 'cpf_client']
