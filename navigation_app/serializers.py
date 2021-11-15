from rest_framework import serializers
from .models import NavigationRecord, Vehicle

class NavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationRecord
        fields = ('latitude', 'longitude', 'vehicle', 'datetime')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('plate',)