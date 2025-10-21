from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = (
        ('Sale', 'Shitje'),
        ('Rent', 'Qira'),
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='properties/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    size = models.IntegerField()
    description = models.TextField()
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)

    def __str__(self):
        return self.title


class SaleProperty(Property):
    class Meta:
        proxy = True
        verbose_name = "Property for Sale"
        verbose_name_plural = "Properties for Sale"


class RentProperty(Property):
    class Meta:
        proxy = True
        verbose_name = "Property for Rent"
        verbose_name_plural = "Properties for Rent"

