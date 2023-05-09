# Importing necessary modules
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BloodDonation, MedicineDonation, DonationAppointment
from .serializers import (
    BloodDonationSerializer,
    MedicineDonationSerializer,
    DonationAppointmentSerializer
)
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

# Creating a view to list and create BloodDonations
@extend_schema(tags=["Donation Management | Blood"])  # adds tags to the schema
@extend_schema(description="List all blood donations", methods=["GET"])  # adds description and methods to the schema
@extend_schema(description="Create a blood donation", methods=["POST"])  # adds description and methods to the schema
class BloodDonationListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BloodDonation.objects.all()  # gets all BloodDonation objects from the database
    serializer_class = BloodDonationSerializer  # uses the BloodDonationSerializer to serialize the data

# Creating a view to retrieve, update, or delete a BloodDonation
@extend_schema(tags=["Donation Management | Blood"])  # adds tags to the schema
@extend_schema(description="Retrieve, update or delete a blood donation", methods=["GET", "PUT", "DELETE"])  # adds description and methods to the schema
class BloodDonationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BloodDonation.objects.all()  # gets all BloodDonation objects from the database
    serializer_class = BloodDonationSerializer  # uses the BloodDonationSerializer to serialize the data

# Creating a view to list and create MedicineDonations
@extend_schema(tags=["Donation Management | Medicine"])  # adds tags to the schema
@extend_schema(description="List all medicine donations", methods=["GET"])  # adds description and methods to the schema
@extend_schema(description="Create a medicine donation", methods=["POST"])  # adds description and methods to the schema
class MedicineDonationListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedicineDonation.objects.all()  # gets all MedicineDonation objects from the database
    serializer_class = MedicineDonationSerializer  # uses the MedicineDonationSerializer to serialize the data

# Creating a view to retrieve, update, or delete a MedicineDonation
@extend_schema(tags=["Donation Management | Medicine"])  # adds tags to the schema
@extend_schema(description="Retrieve, update or delete a medicine donation", methods=["GET", "PUT", "DELETE"])  # adds description and methods to the schema
class MedicineDonationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedicineDonation.objects.all()  # gets all MedicineDonation objects from the database
    serializer_class = MedicineDonationSerializer  # uses the MedicineDonationSerializer to serialize the data

# Creating a view to list and create DonationAppointments
@extend_schema(tags=["Donation Management | Appointment"])  # adds tags to the schema
@extend_schema(description="List all donation appointments", methods=["GET"])  # adds description and methods to the schema
@extend_schema(description="Create a donation appointment", methods=["POST"])  # adds description and methods to the schema
class DonationAppointmentListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DonationAppointment.objects.all()  # gets all DonationAppointment objects from the database
    serializer_class = DonationAppointmentSerializer  # uses the DonationAppointmentSerializer to serialize the data

# Creating a view to retrieve, update, or delete a DonationAppointment
@extend_schema(tags=["Donation Management | Appointment"])
@extend_schema(description="Retrieve, update or delete a donation appointment", methods=["GET", "PUT", "DELETE"])
class DonationAppointmentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DonationAppointment.objects.all() # gets all DonationAppointment objects from the database
    serializer_class = DonationAppointmentSerializer # uses the DonationAppointmentSerializer to serialize the data
