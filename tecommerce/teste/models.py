import uuid
from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.BigAutoField(db_column='id', null=False, primary_key=True)
    created_at = models.DateTimeField(db_column='dt_created_at', null=False, auto_now_add=True)
    modified_at = models.DateTimeField(db_column='dt_modified_at', null=False, auto_now=True)

    active = models.BooleanField(db_column='cs_active', null=False, default=True)

    class Meta:
        abstract = True
        managed = True


class Product(ModelBase):
    description = models.TextField(db_column='tx_description', null=False)
    quantity = models.IntegerField(db_column='nb_quantity', null=False, default=0)

    class Meta:
        db_table = 'product'
        managed = True


class Client(ModelBase):
    name = models.CharField(db_column='tx_name', null=False, max_length=70)
    age = models.IntegerField(db_column='nb_age', null=False)
    rg = models.CharField(db_column='tx_rg', max_length=12, null=False)
    cpf = models.CharField(db_column='tx_cpf', null=False, max_length=12, unique=True)

    class Meta:
        db_table = 'client'
        managed = True


class Employee(ModelBase):
    name = models.CharField(db_column='tx_name', null=False, max_length=70)
    registration = models.CharField(db_column='tx_registration', null=False, max_length=15, unique=True)

    class Meta:
        db_table = 'emplyee'
        managed = True


class Sale(ModelBase):
    nrf = models.CharField(db_column='tx_nrf', null=False, max_length=255)
    employee = models.ForeignKey(Employee, db_column='employee_id', null=False, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, db_column='product_id', null=False, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, db_column='client_id', null=False, on_delete=models.PROTECT)

    class Meta:
        db_table = 'sale'
        managed = True
