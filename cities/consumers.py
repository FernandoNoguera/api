# consumers.py
from .models import City
from .serializers import CityModelSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
)

class CityConsumer(ListModelMixin,GenericAsyncAPIConsumer):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer

