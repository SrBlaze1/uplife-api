from django.db import models
from django.contrib.auth import get_user_model
from recipients.models import Institution, MedicineType, BagType

user = get_user_model()


class BloodDonation(models.Model):
    BLOOD_TYPE_CHOICES = (
        (A_POS := "A+", "A+"),
        (A_NEG := "A-", "A-"),
        (B_POS := "B+", "B+"),
        (B_NEG := "B-", "B-"),
        (AB_POS := "AB+", "AB+"),
        (AB_NEG := "AB-", "AB-"),
        (O_POS := "O+", "O+"),
        (O_NEG := "O-", "O-"),
    )

    recipient = models.ForeignKey(
        Institution, on_delete=models.CASCADE, verbose_name="destinatário"
    )
    donor = models.ForeignKey(user, on_delete=models.PROTECT, verbose_name="doador")
    bag_type = models.ForeignKey(
        BagType, on_delete=models.DO_NOTHING, verbose_name="doador"
    )
    bag_id = models.CharField(max_length=50, verbose_name="identificação da bolsa")
    blood_type = models.CharField(max_length=50, choices=BLOOD_TYPE_CHOICES, verbose_name="tipo sanguíneo")
    quantity = models.PositiveIntegerField(verbose_name="quantidade")
    expiry_date = models.DateField(verbose_name="data de validade")
    validation_date = models.DateTimeField(verbose_name="data de validação")

    class Meta:
        verbose_name = "doação de sangue"
        verbose_name_plural = "doações de sangue"


class MedicineDonation(models.Model):
    recipient = models.ForeignKey(
        Institution, on_delete=models.CASCADE, verbose_name="destinatário"
    )
    donor = models.ForeignKey(user, on_delete=models.PROTECT, verbose_name="doador")
    medicine = models.ForeignKey(
        MedicineType, on_delete=models.DO_NOTHING, verbose_name="medicamento"
    )
    quantity = models.PositiveIntegerField(verbose_name="quantidade")
    compounded = models.BooleanField(default=False, verbose_name="manipulado")
    value = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="valor")
    expiry_date = models.DateField(verbose_name="data de validade")
    validation_date = models.DateTimeField(verbose_name="data de validação")

    class Meta:
        verbose_name = "doação de medicamento"
        verbose_name_plural = "doações de medicamento"


class DonationAppointment(models.Model):
    DONATION_TYPE_CHOICES = (
        (MED := "MED", "Medicamento"),
        (SAN := "SAN", "Sangue"),
    )
    recipient = models.ForeignKey(
        Institution, on_delete=models.CASCADE, verbose_name="destinatário"
    )
    donor = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name="doador")
    donation_type = models.CharField(
        max_length=50, choices=DONATION_TYPE_CHOICES, verbose_name="tipo de doação"
    )
    scheduled_date = models.DateTimeField(verbose_name="data agendada")

    class Meta:
        verbose_name = "agendamento de doação"
        verbose_name_plural = "agendamentos de doação"
