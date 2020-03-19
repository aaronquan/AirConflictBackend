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
    bounding_box = serializers.SerializerMethodField()
    parts = serializers.SerializerMethodField()
    class Meta:
        model = MapShape
        fields = ['sovereignty', 'admin', 'continent', 'bounding_box', 'parts']
                  #'min_longitude', 'min_latitude', 'max_longitude', 'max_latitude']
    def get_bounding_box(self, obj):
        return obj.bounding_box()
    def get_parts(self, obj):
        parts = obj.parts()
        return [{'points': MapPointSerializer(part['points'], many=True).data, 'bounding_box': part['bounding_box']} for part in parts]

