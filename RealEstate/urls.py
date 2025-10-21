from django.urls import path
from . import views 


urlpatterns = [

    path('' , views.home, name='homePage'),
    path('sales/', views.sales, name='salesPage'),
    path('rental/', views.rental, name='rentalPage'),
    path('agent/', views.agent, name='agentPage'),
    path('contact/', views.contact, name='contactPage'),
]