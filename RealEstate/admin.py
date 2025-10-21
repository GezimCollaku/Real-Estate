from django.contrib import admin
from .models import SaleProperty, RentProperty

@admin.register(SaleProperty)
class SalePropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rooms', 'bathrooms', 'size')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(property_type='Sale')

@admin.register(RentProperty)
class RentPropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rooms', 'bathrooms', 'size')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(property_type='Rent')
    


