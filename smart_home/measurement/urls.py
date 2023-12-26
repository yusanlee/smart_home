from django.urls import path
from .views import SensorList, SensorCreate, ModifySensor, MeasurementCreate, SensorView

urlpatterns = [
    path('list/', SensorList.as_view()),
    path('create/', SensorCreate.as_view()),
    path('modify/<pk>', ModifySensor.as_view()),
    path('measurement/', MeasurementCreate.as_view()),
    path('sensor/<pk>', SensorView.as_view()),

]