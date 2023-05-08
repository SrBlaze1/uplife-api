from django.db import models
from localflavor.br.models import BRStateField, BRCNPJField, BRPostalCodeField


class Institution(models.Model):
    cnpj = BRCNPJField(verbose_name="CNPJ", unique=True)
    corporate_name = models.CharField(max_length=60, verbose_name="razão social")
    address = models.CharField(max_length=60, verbose_name="logradouro")
    district = models.CharField(max_length=30, verbose_name="bairro")
    city = models.CharField(max_length=30, verbose_name="cidade")
    state = BRStateField(verbose_name="estado")
    zip_code = BRPostalCodeField(verbose_name="CEP", unique=True)

    class Meta:
        verbose_name = "instituição"
        verbose_name_plural = "instituições"

    def __str__(self):
        return f"{self.corporate_name} ({self.cnpj})"


class BagType(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome")
    specification = models.CharField(max_length=50, verbose_name="especificação", null=True)
    capacity = models.PositiveIntegerField(verbose_name="capacidade")

    class Meta:
        verbose_name = "tipo de bolsa"
        verbose_name_plural = "tipos de bolsas"

    def __str__(self):
        return f"{self.name} - {self.specification} ({self.capacity}ml)"


class MedicineType(models.Model):
    trade_name = models.CharField(max_length=50, verbose_name="nome comercial")
    generic_name = models.CharField(max_length=50, verbose_name="nome genérico", null=True)
    risk_factor = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="fator de risco"
    )

    class Meta:
        verbose_name = "tipo de medicamento"
        verbose_name_plural = "tipos de medicamentos"

    def __str__(self):
        if self.generic_name:
            return f"{self.trade_name} ({self.generic_name})"
        else:
            return self.trade_name if self.trade_name else self.generic_name
