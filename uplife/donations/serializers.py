from rest_framework import serializers
from .models import (
    BloodDonation,
    MedicineDonation,
    DonationAppointment,
)

# Serializer for BloodDonation model
class BloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonation # Set the model for this serializer
        fields = "__all__" # Include all fields in the serialized representation of the model


# Serializer for MedicineDonation model
class MedicineDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDonation # Set the model for this serializer
        fields = "__all__" # Include all fields in the serialized representation of the model


# Serializer for DonationAppointment model
class DonationAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationAppointment # Set the model for this serializer
        fields = "__all__" # Include all fields in the serialized representation of the model
