from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Institution, BagType, MedicineType
from .serializers import (
    InstitutionSerializer,
    BagTypeSerializer,
    MedicineTypeSerializer,
)
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated


@extend_schema(tags=["Recipient Management | Institution"])
@extend_schema(description="List all institutions", methods=["GET"])
@extend_schema(description="Create an institution", methods=["POST"])
class InstitutionListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


@extend_schema(tags=["Recipient Management | Institution"])
@extend_schema(
    description="Retrieve, update or delete an institution",
    methods=["GET", "PUT", "DELETE"],
)
class InstitutionDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


@extend_schema(tags=["Recipient Management | Bag"])
@extend_schema(description="List all bag types", methods=["GET"])
@extend_schema(description="Create a bag type", methods=["POST"])
class BagTypeListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BagType.objects.all()
    serializer_class = BagTypeSerializer


@extend_schema(tags=["Recipient Management | Bag"])
@extend_schema(
    description="Retrieve, update or delete a bag type",
    methods=["GET", "PUT", "DELETE"],
)
class BagTypeDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BagType.objects.all()
    serializer_class = BagTypeSerializer


@extend_schema(tags=["Recipient Management | Medicine"])
@extend_schema(description="List all medicine types", methods=["GET"])
@extend_schema(description="Create a medicine type", methods=["POST"])
class MedicineTypeListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedicineType.objects.all()
    serializer_class = MedicineTypeSerializer


@extend_schema(tags=["Recipient Management | Medicine"])
@extend_schema(
    description="Retrieve, update or delete a medicine type",
    methods=["GET", "PUT", "DELETE"],
)
class MedicineTypeDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedicineType.objects.all()
    serializer_class = MedicineTypeSerializer
