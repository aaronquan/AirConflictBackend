
from django.core.management.base import BaseCommand

from flightapi.models import MapShape, MapPoint, ShapePart
from flightapi.serializers import *
from flightapi.general import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        #obj = MapShape.objects.get(pk=1)
        #parts = obj.parts()
        #for part in parts:
        #    ser = MapPointSerializer(part, many=True)
        #    print(ser.data)
        #mss = MapShapeSerializer(obj)
        #print(mss.data)

        #print(MapShape.)
        #print(MapShape.longitude_normal.all())

        for obj in MapShape.objects.all():
            if(obj.min_longitude > obj.max_longitude):
                print({'minl': obj.min_longitude, 'maxl': obj.max_longitude})
        obj = MapShape.objects.get(admin="Russia")
        print({'minl': obj.min_longitude, 'maxl': obj.max_longitude, 'minl2': obj.max_latitude})
