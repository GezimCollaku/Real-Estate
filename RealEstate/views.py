from django.shortcuts import render 
from .models import SaleProperty, RentProperty 

def home(request):
    return render(request, 'home.html')  

def sales(request):
    properties = SaleProperty.objects.filter(property_type='Sale')
    return render(request, 'sales.html', {'properties': properties})

def rental(request):
    properties = RentProperty.objects.filter(property_type='Rent')
    return render(request, 'rental.html', {'properties': properties})

def agent(request):
    return render(request, 'agent.html')

def contact(request):
    return render(request, 'contact.html')

