from django.urls import path
from .views import SensorAPIView, SensorUpdateAPIView, MeasurementAPIView, SensorListAPIView,SensorMeasurementAPIView
urlpatterns = [
    path('create_sensor/', SensorAPIView.as_view()),
    path('change_sensor/<pk>/', SensorUpdateAPIView.as_view()),
    path('create_measurement/', MeasurementAPIView.as_view()),
    path('sensor_list/', SensorListAPIView.as_view()),
    path('info_sensor/<pk>/', SensorMeasurementAPIView.as_view()),
]
