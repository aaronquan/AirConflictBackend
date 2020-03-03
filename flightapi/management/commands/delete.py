from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="model name")
        parser.add_argument('app_name', type=str, help="django app name that the model is connected to")
    def handle(self, *args, **options):
        _model = apps.get_model(options['app_name'], options['model_name'])
        _model.objects.all().delete()