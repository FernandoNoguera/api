# base
from django.urls import path, include
from rest_framework_nested import routers
from .views import CityModelViewSet
# routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"^cities/$", consumers.CityConsumer.as_asgi()),
]



app_name = 'cities'

router = routers.SimpleRouter()
router.register(r'', CityModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]