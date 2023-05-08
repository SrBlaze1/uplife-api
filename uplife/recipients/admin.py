from django.contrib import admin
from .models import Institution, BagType, MedicineType

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'corporate_name', 'city', 'state')
    search_fields = ('cnpj', 'corporate_name', 'city', 'state')

@admin.register(BagType)
class BagTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'specification', 'capacity')
    search_fields = ('name', 'specification', 'capacity')

@admin.register(MedicineType)
class MedicineTypeAdmin(admin.ModelAdmin):
    list_display = ('trade_name', 'generic_name', 'risk_factor')
    search_fields = ('trade_name', 'generic_name', 'risk_factor')
