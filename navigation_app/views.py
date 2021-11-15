from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import NavigationRecord, Vehicle
from .serializers import NavigationSerializer, VehicleSerializer

from datetime import datetime, timedelta


@csrf_exempt
def NavigationApi(request, id=0):
    if request.method == 'GET':
        thetime = datetime.now() - timedelta(hours=48)
        results = NavigationRecord.objects.filter(datetime__gte=thetime).order_by('vehicle','-datetime').distinct('vehicle')
        records = results #NavigationRecord.objects.all()
        records_serializer = NavigationSerializer(records, many=True)
        return JsonResponse(records_serializer.data, safe=False)
    elif request.method == 'POST':
        record_data = JSONParser().parse(request)
        records_serializer = NavigationSerializer(data=record_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        record_data = JSONParser().parse(request)
        record = NavigationRecord.objects.get(id=record_data['id'])
        records_serializer = NavigationSerializer(record, data=record_data)
        if records_serializer.is_valid():
            records_serializer.save()
            return JsonResponse("Updated Succesfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        record = NavigationRecord.objects.get(id=id)
        record.delete()
        return JsonResponse("Deleted Succesfully", safe=False)



@csrf_exempt
def VehicleApi(request, id=0):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        vehicles_serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(vehicles_serializer.data, safe=False)
    elif request.method == 'POST':
        vehicle_data = JSONParser().parse(request)
        vehicles_serializer = VehicleSerializer(data=vehicle_data)
        if vehicles_serializer.is_valid():
            vehicles_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        vehicle_data = JSONParser().parse(request)
        vehicle = Vehicle.objects.get(id=vehicle_data['id'])
        vehicles_serializer = VehicleSerializer(vehicle, data=vehicle_data)
        if vehicles_serializer.is_valid():
            vehicles_serializer.save()
            return JsonResponse("Updated Succesfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        vehicle = Vehicle.objects.get(id=id)
        vehicle.delete()
        return JsonResponse("Deleted Succesfully", safe=False)