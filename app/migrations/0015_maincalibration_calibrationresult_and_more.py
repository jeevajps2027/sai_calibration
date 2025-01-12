# Generated by Django 5.1.1 on 2024-11-09 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_workorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCalibration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_num', models.CharField(max_length=100, unique=True)),
                ('work_order', models.CharField(max_length=100, unique=True)),
                ('date_of_issue', models.DateField(blank=True, null=True)),
                ('date_of_calibration', models.DateField(blank=True, null=True)),
                ('next_calibration', models.DateField(blank=True, null=True)),
                ('customer_address', models.TextField(blank=True)),
                ('range', models.CharField(blank=True, max_length=100)),
                ('least_count', models.CharField(blank=True, max_length=100)),
                ('identification_no', models.CharField(blank=True, max_length=100)),
                ('si_no', models.CharField(blank=True, max_length=100)),
                ('make', models.CharField(blank=True, max_length=100)),
                ('customer_ref', models.CharField(blank=True, max_length=100)),
                ('date_calib', models.DateField(blank=True, null=True)),
                ('date_of_receipt', models.DateField(blank=True, null=True)),
                ('calib_procedure_no', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('inward_no', models.CharField(blank=True, max_length=100)),
                ('environment', models.CharField(blank=True, max_length=100)),
                ('uncertainty', models.CharField(blank=True, max_length=100)),
                ('calib_engineer', models.CharField(blank=True, max_length=100)),
                ('quality_manager', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CalibrationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_id', models.CharField(max_length=50)),
                ('parameter', models.CharField(blank=True, max_length=100)),
                ('ref_size', models.CharField(blank=True, max_length=100)),
                ('nominal', models.CharField(blank=True, max_length=100)),
                ('observation_size', models.CharField(blank=True, max_length=100)),
                ('error', models.CharField(blank=True, max_length=100)),
                ('main_calibration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='app.maincalibration')),
            ],
        ),
        migrations.CreateModel(
            name='CalibrationEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('master_name', models.CharField(blank=True, max_length=100)),
                ('id_no', models.CharField(blank=True, max_length=100)),
                ('calibration_no', models.CharField(blank=True, max_length=100)),
                ('valid_upto', models.DateField(blank=True, null=True)),
                ('traceability', models.CharField(blank=True, max_length=100)),
                ('main_calibration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='app.maincalibration')),
            ],
        ),
    ]
