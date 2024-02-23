# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView,RetrieveAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer

class SensorAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorListAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorMeasurementAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer