from django.contrib import admin
from django.urls import path

from measurement.views import SensorListView, SensorView, MeasurementListView, redirect_start

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_start),
    path('sensor/', SensorListView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurement/', MeasurementListView.as_view()),
]
