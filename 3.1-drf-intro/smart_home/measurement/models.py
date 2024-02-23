from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_meas')
    temperature = models.FloatField()
    data_time = models.DateTimeField(auto_now=True)
