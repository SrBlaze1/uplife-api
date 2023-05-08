from django.contrib import admin
from .models import BloodDonation, MedicineDonation, DonationAppointment


@admin.register(BloodDonation)
class BloodDonationAdmin(admin.ModelAdmin):
    list_display = ("recipient", "donor", "bag_type", "bag_id", "blood_type", "quantity", "validation_date")


@admin.register(MedicineDonation)
class MedicineDonationAdmin(admin.ModelAdmin):
    list_display = ("recipient", "donor", "medicine", "quantity", "compounded", "value", "expiry_date")


@admin.register(DonationAppointment)
class DonationAppointmentAdmin(admin.ModelAdmin):
    list_display = ("recipient", "donor", "donation_type", "scheduled_date")
