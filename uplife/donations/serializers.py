from rest_framework import serializers
from .models import (
    BloodDonation,
    MedicineDonation,
    DonationAppointment,
)


class BloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonation
        fields = "__all__"


class MedicineDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDonation
        fields = "__all__"


class DonationAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationAppointment
        fields = "__all__"
