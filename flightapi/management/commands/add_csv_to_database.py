from django.core.management.base import BaseCommand
from django.apps import apps
import csv

# global parser for csv files which contain a header

class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")
        parser.add_argument('model_name', type=str, help="model name")
        parser.add_argument('app_name', type=str, help="django app name that the model is connected to")

    def handle(self, *args, **options):
        file_path = options['path']
        _model = apps.get_model(options['app_name'], options['model_name'])
        model_fields = [f.name for f in _model._meta.get_fields()]
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            header = next(reader)
            for row in reader:
                _object_dict = {key: value for key, value in zip(header, row)}
                _filtered_object_dict = {k: _object_dict[k] for k in model_fields}
                m = _model(**_filtered_object_dict)
                m.save()
                #_model.objects.create(**_filtered_object_dict)
