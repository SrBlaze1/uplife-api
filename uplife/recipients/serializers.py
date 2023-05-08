from rest_framework import serializers
from .models import (
    Institution,
    BagType,
    MedicineType,
)


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"


class BagTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BagType
        fields = "__all__"


class MedicineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineType
        fields = "__all__"
