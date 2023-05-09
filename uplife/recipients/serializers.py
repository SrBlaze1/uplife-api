from rest_framework import serializers
from .models import (
    Institution,
    BagType,
    MedicineType,
)

# Serializer for the Institution model
class InstitutionSerializer(serializers.ModelSerializer):
    # Define the model and all of its fields to be included in the serialization
    class Meta:
        model = Institution
        fields = "__all__"

# Serializer for the BagType model
class BagTypeSerializer(serializers.ModelSerializer):
    # Define the model and all of its fields to be included in the serialization
    class Meta:
        model = BagType
        fields = "__all__"

# Serializer for the MedicineType model
class MedicineTypeSerializer(serializers.ModelSerializer):
    # Define the model and all of its fields to be included in the serialization
    class Meta:
        model = MedicineType
        fields = "__all__"
