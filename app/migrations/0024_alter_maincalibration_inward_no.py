# Generated by Django 5.1.1 on 2024-11-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_maincalibration_calibrationresult_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincalibration',
            name='inward_no',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]