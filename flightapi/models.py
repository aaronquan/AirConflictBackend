from django.db import models
from django.db.models import Q, F

class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    icao = models.CharField(max_length=4, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.SmallIntegerField()
    timezone = models.CharField(max_length=40)

#class Route(models.Model):
#	origin = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='origin') # check on delete
#	destination = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='destination') 

#class Flight(models.Model):
#    flightid = models.CharField(max_length=100, primary_key=True)
#    route = models.ForeignKey(Route, on_delete=models.CASCADE)
#    ident = models.CharField(max_length=10)
#    actual_takeoff_time = models.DateTimeField()
#    actual_landing_time = models.DateTimeField()
#    scheduled_takeoff_time = models.DateTimeField()
#    scheduled_landing_time = models.DateTimeField()

## store all fixed tracklogs
#class TracklogEntry(models.Model):
#    related_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight')
#    seq_no = models.PositiveIntegerField() # index of tracklog
#    time = models.IntegerField() # seconds after take off (possible negative)
#    latitude = models.FloatField()
#    longitude = models.FloatField()
#    direction = models.PositiveSmallIntegerField() #double check if all positive
#    speed = models.PositiveSmallIntegerField() # check if all small (some possible errors)
#    altitude = models.PositiveSmallIntegerField()
#    climb_rate = models.SmallIntegerField()
#    facility = models.CharField()

#class MapLongitudeCrossManager(models.Manager):
#    def get_queryset(self):
#        return super().get_queryset().filter(min_longitude__gt=F('max_longitude'))

#class MapLongitudeNormalManager(models.Manager):
#    def get_queryset(self):
#        return super().get_queryset().filter(min_longitude__lte=F('max_longitude'))

# map models
# check these models (don't migrate yet)
class MapShape(models.Model):
    #shapeType = models.IntegerField() #possible choices (lookup shapefile format) all same not needed
    #parts, could have separate shape for multiple part shapes (check format and other variables of shape)
    #bounding fields (bbox)
    sovereignty = models.CharField(max_length=32)
    admin = models.CharField(max_length=35)
    continent  = models.CharField(max_length=23)
    min_longitude = models.FloatField()
    max_longitude = models.FloatField()
    min_latitude = models.FloatField()
    max_latitude = models.FloatField()
    #objects = models.Manager()
    #longitude_cross = MapLongitudeCrossManager() # set for when longitude passes 180 to -180 line
    #longitude_normal = MapLongitudeNormalManager() # set for when longitude does not pass the 180 to -180 line
    #all models have min_longitude < max_longitude i.e. -180 to 180 if crosses 180 line
    def parts(self):
        sets = []
        last = self.mappoint.count()
        for part in self.shapepart.all().order_by('-index'):
            points = self.mappoint.filter(seq_no__gte=part.index,seq_no__lt=last)
            last = part.index
            sets.append(points)
        return sets
    def inside_bound(self, min_lon, max_lon, min_lat, max_lat):
        inside_lon = coordinate.is_longitude_intersecting(min_lon, max_lon, self.min_longitude, self.max_longitude)
        inside_lat = coordinate.is_latitude_intersecting(min_lat, max_lat, self.min_latitude, self.max_latitude)
        return inside_lon and inside_lat

class MapPoint(models.Model):
    shape = models.ForeignKey(MapShape, on_delete=models.CASCADE, related_name='mappoint') # check on_delete
    seq_no = models.PositiveIntegerField() # index of point
    longitude = models.FloatField()
    latitude = models.FloatField()

class ShapePart(models.Model):
    shape = models.ForeignKey(MapShape, on_delete=models.CASCADE, related_name='shapepart')
    index = models.PositiveIntegerField() #index of map point (seq_no); divides map points into parts

