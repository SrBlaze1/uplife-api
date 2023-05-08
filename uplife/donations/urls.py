from django.urls import path
from .views import (
    BloodDonationListView,
    BloodDonationDetailView,
    MedicineDonationListView,
    MedicineDonationDetailView,
    DonationAppointmentListView,
    DonationAppointmentDetailView,
)

urlpatterns = [
    path('blood-donation/', BloodDonationListView.as_view(), name='blood_donation_list_create'),
    path('blood-donation/<int:pk>/', BloodDonationDetailView.as_view(), name='blood_donation_detail'),
    path('medicine-donation/', MedicineDonationListView.as_view(), name='medicine_donation_list_create'),
    path('medicine-donation/<int:pk>/', MedicineDonationDetailView.as_view(), name='medicine_donation_detail'),
    path('donation-appointment/', DonationAppointmentListView.as_view(), name='donation_appointment_list_create'),
    path('donation-appointment/<int:pk>/', DonationAppointmentDetailView.as_view(), name='donation_appointment_detail'),
]
