from rest_framework.viewsets import ModelViewSet
from .models import (
    City,
)
from .serializers import (
    CityModelSerializer,
)


class CityModelViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer
    search_fields = ('name',)
    http_method_names = ['get', 'head','post','options']