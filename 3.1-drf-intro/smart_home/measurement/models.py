from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время измерения')
    image = models.ImageField(max_length=255, blank=True, default='')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'{self.sensor.name}: {self.temperature} ({self.created_at})'
