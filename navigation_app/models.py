from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=12)

    def __str__(self):
        return '{}'.format(self.plate)


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='plaka')
    datetime = models.DateTimeField()
    latitude = models.DecimalField(max_digits=12, decimal_places=3)
    longitude = models.DecimalField(max_digits=12, decimal_places=3)

    def __str__(self):
        return 'Latitude: {}, Longitude: {}, Vehicle: {}, Date & Time: {}'.format(self.latitude, self.longitude, self.vehicle, self.datetime)
    

