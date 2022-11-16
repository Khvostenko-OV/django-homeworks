from rest_framework import serializers

from measurement.models import Sensor, Measurement


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__' #['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
