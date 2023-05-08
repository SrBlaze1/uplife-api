from django.urls import path
from .views import (
    InstitutionListView,
    InstitutionDetailView,
    BagTypeListView,
    BagTypeDetailView,
    MedicineTypeListView,
    MedicineTypeDetailView
)

urlpatterns = [
    path('institutions/', InstitutionListView.as_view(), name='institution_list_create'),
    path('institutions/<int:pk>/', InstitutionDetailView.as_view(), name='institution_retrieve_update_destroy'),
    path('bag_types/', BagTypeListView.as_view(), name='bag_type_list_create'),
    path('bag_types/<int:pk>/', BagTypeDetailView.as_view(), name='bag_type_retrieve_update_destroy'),
    path('medicine_types/', MedicineTypeListView.as_view(), name='medicine_type_list_create'),
    path('medicine_types/<int:pk>/', MedicineTypeDetailView.as_view(), name='medicine_type_retrieve_update_destroy'),
]
