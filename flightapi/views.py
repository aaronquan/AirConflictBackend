from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

import json

from .models import Airport
from .serializers import *
from .pagination import *

from flightapi.general import *

class AirportViewSet(viewsets.ModelViewSet):
    serializer_class = AirportSerializer
    queryset = Airport.objects.all()
    pagination_class = LargePageNumberPaginationWithCount

class AusAirportViewSet(viewsets.ModelViewSet):
    serializer_class = AirportSerializer
    queryset = Airport.aus_airports.all()
    pagination_class = SmallPageNumberPaginationWithCount

class MapFilter(filters.FilterSet):
    class Meta:
        model = MapShape
        fields = {
            'sovereignty': ['iexact'],
            'admin': ['iexact'],
            'continent': ['iexact'],
            #'min_longitude': ['gte','lte'],
            #'min_latitude': ['gte','lte'],
            #'max_longitude': ['gte','lte'],
            #'max_latitude': ['gte','lte'],
        }

class MapViewSet(viewsets.ModelViewSet):
    serializer_class = MapShapeSerializer
    pagination_class = SmallPageNumberPaginationWithCount
    queryset = MapShape.objects.all()
    #filter_backends = [MapRegionFilter]
    filterset_class = MapFilter
    #filterset_fields = ['admin']

# filters all map shapes within the area given by a bounding coordinate box (min_longitude, min_latitude, max_longitude, max_latitude)
# min_longitude can be > max_longitude, then take the area min_longitude to 180 and -180 to max_longitude
class MapAreaViewSet(viewsets.ModelViewSet):
    serializer_class = MapShapeSerializer
    pagination_class = SmallPageNumberPaginationWithCount
    def get_queryset(self):
        min_lon = self.request.query_params.get('min_longitude', None)
        max_lon = self.request.query_params.get('max_longitude', None)
        min_lat = self.request.query_params.get('min_latitude', None)
        max_lat = self.request.query_params.get('max_latitude', None)
        q_set = MapShape.objects.none()
        map_shapes = MapShape.objects.all().order_by('admin')
        if all(var is not None for var in [min_lon, max_lon, min_lat, max_lat]):
            if min_lon < max_lon:
               q_set = map_shapes.filter(min_longitude__lt=max_lon, max_longitude__gt=min_lon, 
                                         min_latitude__lt=max_lat, max_latitude__gt=min_lat)
            elif min_lon > max_lon:
                q_set = map_shapes.filter(Q(min_longitude__gt=max_lon) | Q(max_longitude__gt=min_lon), 
                                          Q(min_latitude__lt=max_lat, max_latitude__gt=min_lat))
        return q_set