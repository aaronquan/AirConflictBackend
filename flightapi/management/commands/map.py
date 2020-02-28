from django.core.management.base import BaseCommand

from flightapi.models import MapShape, MapPoint, ShapePart

import shapefile

#fname = 'countries_50m/ne_50m_admin_0_countries_lakes'
#path flightapi/data/map/countries_50m/ne_50m_admin_0_countries_lakes

class Command(BaseCommand):
    help = 'Adding a map file to the database'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")
    def handle(self, *args, **options):
        file_path = options['path']
        sf = shapefile.Reader(file_path)
        #records = sf.records() # contains fields
        #shapes = sf.shapes()
        for sr in sf.iterShapeRecords():
            record = sr.record
            shape = sr.shape
            map_shape = {'sovereignty': record['SOVEREIGNT'], 'admin': record['ADMIN'], 'continent': record['CONTINENT'],
                         'min_longitude': shape.bbox[0] , 'min_latitude': shape.bbox[1], 
                         'max_longitude': shape.bbox[2], 'max_latitude': shape.bbox[3]}
            print(map_shape)
            ms = MapShape(**map_shape)
            ms.save()
            for i, point in enumerate(sr.shape.points):
                map_point = {'shape': ms, 'longitude':point[0], 'latitude':point[1], 'seq_no':i}
                #print(map_point)
                mp = MapPoint(**map_point)
                mp.save()
                #break
            for part in sr.shape.parts:
                shape_part = {'shape': ms, 'index': part}
                #print(shape_part)
                sp = ShapePart(**shape_part)
                sp.save()
                #break
            #break