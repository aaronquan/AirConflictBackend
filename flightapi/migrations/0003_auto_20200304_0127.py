# Generated by Django 2.2.10 on 2020-03-03 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightapi', '0002_mappoint_mapshape_shapepart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappoint',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mappoint', to='flightapi.MapShape'),
        ),
        migrations.AlterField(
            model_name='shapepart',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shapepart', to='flightapi.MapShape'),
        ),
    ]