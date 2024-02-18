from django.db import models
from utils.models import CommonModel

class Client(CommonModel):
    name = models.CharField(max_length=120)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Carrier(CommonModel):
    name = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Package(CommonModel):
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimensions = models.CharField(max_length=50)
    origin_address = models.TextField()
    destination_address = models.TextField()
    delivery_status = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)

    def __str__(self):
        return f"Package #{self.id}"



