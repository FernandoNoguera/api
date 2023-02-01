from rest_framework import serializers
from statistics import mean 
from .models import (
    City,
)
from utils.weather import (
    get_forecast,
    get_city_weather,
)



class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    def last_7_days_average(self, data):
        return mean([num['main']['temp'] for num in data['list']])

    def to_representation(self, instance):
        data = super().to_representation(instance)
        response = get_city_weather(data['name'])
        forecast = get_forecast(data['name'])
        data = {
            'id': data['id'],
            'city':response['name'],
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['main'],
            'last_7_days_average':self.last_7_days_average(forecast),
        }
        return data