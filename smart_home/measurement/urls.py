from django.urls import path

from measurement.views import CreateSensor, UpdateSensor, CreateMeasurement

urlpatterns = [
    path('sensors/', CreateSensor.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
