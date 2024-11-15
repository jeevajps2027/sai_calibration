# Generated by Django 5.1.1 on 2024-11-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_workorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('wo_date', models.CharField(max_length=50)),
                ('work_order_no', models.CharField(max_length=50)),
                ('customer_po_no', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_ref_date', models.CharField(blank=True, max_length=50, null=True)),
                ('order_type', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_address', models.TextField(blank=True, null=True)),
                ('inward_no', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('hsn', models.CharField(blank=True, max_length=100, null=True)),
                ('sr_no', models.CharField(blank=True, max_length=100, null=True)),
                ('id_no', models.CharField(blank=True, max_length=100, null=True)),
                ('range', models.CharField(blank=True, max_length=100, null=True)),
                ('make', models.CharField(blank=True, max_length=100, null=True)),
                ('channels', models.CharField(max_length=255)),
            ],
        ),
    ]