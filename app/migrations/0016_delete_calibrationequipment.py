# Generated by Django 5.1.1 on 2024-11-09 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_maincalibration_calibrationresult_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CalibrationEquipment',
        ),
    ]