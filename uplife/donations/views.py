from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BloodDonation, MedicineDonation, DonationAppointment
from .serializers import (
    BloodDonationSerializer,
    MedicineDonationSerializer,
    DonationAppointmentSerializer
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Donation Management | Blood"])
@extend_schema(description="List all blood donations", methods=["GET"])
@extend_schema(description="Create a blood donation", methods=["POST"])
class BloodDonationListView(ListCreateAPIView):
    queryset = BloodDonation.objects.all()
    serializer_class = BloodDonationSerializer


@extend_schema(tags=["Donation Management | Blood"])
@extend_schema(description="Retrieve, update or delete a blood donation", methods=["GET", "PUT", "DELETE"])
class BloodDonationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BloodDonation.objects.all()
    serializer_class = BloodDonationSerializer


@extend_schema(tags=["Donation Management | Medicine"])
@extend_schema(description="List all medicine donations", methods=["GET"])
@extend_schema(description="Create a medicine donation", methods=["POST"])
class MedicineDonationListView(ListCreateAPIView):
    queryset = MedicineDonation.objects.all()
    serializer_class = MedicineDonationSerializer


@extend_schema(tags=["Donation Management | Medicine"])
@extend_schema(description="Retrieve, update or delete a medicine donation", methods=["GET", "PUT", "DELETE"])
class MedicineDonationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MedicineDonation.objects.all()
    serializer_class = MedicineDonationSerializer


@extend_schema(tags=["Donation Management | Appointment"])
@extend_schema(description="List all donation appointments", methods=["GET"])
@extend_schema(description="Create a donation appointment", methods=["POST"])
class DonationAppointmentListView(ListCreateAPIView):
    queryset = DonationAppointment.objects.all()
    serializer_class = DonationAppointmentSerializer


@extend_schema(tags=["Donation Management | Appointment"])
@extend_schema(description="Retrieve, update or delete a donation appointment", methods=["GET", "PUT", "DELETE"])
class DonationAppointmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DonationAppointment.objects.all()
    serializer_class = DonationAppointmentSerializer
