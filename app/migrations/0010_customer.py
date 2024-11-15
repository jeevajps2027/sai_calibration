# Generated by Django 5.1.1 on 2024-10-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('primary_contact_person', models.CharField(max_length=255)),
                ('secondary_contact_person', models.CharField(max_length=255)),
                ('primary_email', models.EmailField(max_length=254)),
                ('secondary_email', models.EmailField(max_length=254)),
                ('primary_phone_no', models.CharField(max_length=15)),
                ('secondary_phone_no', models.CharField(max_length=15)),
                ('gst_no', models.CharField(max_length=15)),
                ('primary_dept', models.CharField(max_length=255)),
                ('secondary_dept', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
    ]