# Importing necessary modules
from django.db import models
from localflavor.br.models import BRStateField, BRCNPJField, BRPostalCodeField


# Institution model to store details about institutions
class Institution(models.Model):
    # Field to store CNPJ with validation
    cnpj = BRCNPJField(verbose_name="CNPJ", unique=True)
    # Field to store corporate name
    corporate_name = models.CharField(max_length=60, verbose_name="razão social")
    # Field to store address
    address = models.CharField(max_length=60, verbose_name="logradouro")
    # Field to store district
    district = models.CharField(max_length=30, verbose_name="bairro")
    # Field to store city
    city = models.CharField(max_length=30, verbose_name="cidade")
    # Field to store state with validation
    state = BRStateField(verbose_name="estado")
    # Field to store zip code with validation
    zip_code = BRPostalCodeField(verbose_name="CEP", unique=True)

    # Defining a string representation of the object
    def __str__(self):
        return f"{self.corporate_name} ({self.cnpj})"

    # Setting model metadata
    class Meta:
        verbose_name = "instituição"  # Singular name for the model
        verbose_name_plural = "instituições"  # Plural name for the model


# BagType model to store details about bag types
class BagType(models.Model):
    recipient = models.ForeignKey(
        Institution, on_delete=models.CASCADE, verbose_name="instituição"
    )
    # Field to store bag type name
    name = models.CharField(max_length=50, verbose_name="nome")
    # Field to store bag type specification
    specification = models.CharField(
        max_length=50, verbose_name="especificação", null=True
    )
    # Field to store bag type capacity
    capacity = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="capacidade"
    )

    # Defining a string representation of the object
    def __str__(self):
        return f"{self.name} - {self.specification} ({self.capacity}ml)"

    # Setting model metadata
    class Meta:
        verbose_name = "tipo de bolsa"  # Singular name for the model
        verbose_name_plural = "tipos de bolsas"  # Plural name for the model


# MedicineType model to store details about medicine types
class MedicineType(models.Model):
    recipient = models.ForeignKey(
        Institution, on_delete=models.CASCADE, verbose_name="instituição"
    )
    # Field to store medicine trade name
    trade_name = models.CharField(max_length=50, verbose_name="nome comercial")
    # Field to store medicine generic name
    generic_name = models.CharField(
        max_length=50, verbose_name="nome genérico", null=True
    )
    # Field to store whether medicine has risk factor
    risk_factor = models.BooleanField(verbose_name="fator de risco")

    # Defining a string representation of the object
    def __str__(self):
        return self.trade_name if self.trade_name else self.generic_name

    # Setting model metadata
    class Meta:
        verbose_name = "tipo de medicamento"  # Singular name for the model
        verbose_name_plural = "tipos de medicamentos"  # Plural name for the model
