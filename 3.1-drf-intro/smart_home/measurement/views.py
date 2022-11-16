from django.forms import model_to_dict
from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorListSerializer, SensorSerializer, MeasurementListSerializer


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = SensorListSerializer

    def post(self, request):
        new_sensor = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'POST': model_to_dict(new_sensor)})

    def put(self, request):
        sensor_id = request.data['id']
        put_sensor = Sensor.objects.get(pk=sensor_id)
        put_sensor.name=request.data['name']
        put_sensor.description=request.data['description']
        put_sensor.save()
        return Response({'PUT': model_to_dict(put_sensor)})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementListView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementListSerializer

    def post(self, request):
        new_measurement = Measurement.objects.create(
            temperature=request.data['temperature'],
            image=request.data.get('image'),
            sensor=Sensor.objects.get(pk=request.data['sensor'])
        )
        return Response({'POST': model_to_dict(new_measurement)})


def redirect_start(request):
    return redirect('sensor/')
