from rest_framework import serializers
from .models import *

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class MapPointSerializer(serializers.ModelSerializer):
    #class Meta:
    #    model = MapPoint
    #    fields = ['longitude', 'latitude']
    def to_representation(self, instance):
        return [instance.longitude, instance.latitude]

class MapShapeSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()
    class Meta:
        model = MapShape
        fields = ['sovereignty', 'admin', 'continent','min_longitude', 
                  'min_latitude', 'max_longitude', 'max_latitude', 'points']

    def get_points(self, obj):
        parts = obj.parts()
        return [MapPointSerializer(part, many=True).data for part in parts]

