from django.contrib import admin

from measurement.models import Sensor, Measurement


class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = (MeasurementInline,)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
