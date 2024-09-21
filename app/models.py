from django.db import models


# Customer model
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    primary_contact_person = models.CharField(max_length=255)
    secondary_contact_person = models.CharField(max_length=255)
    primary_email = models.EmailField()
    secondary_email = models.EmailField()
    primary_phone_no = models.CharField(max_length=15)
    secondary_phone_no = models.CharField(max_length=15)
    gst_no = models.CharField(max_length=15)
    dept = models.CharField(max_length=255)
    address = models.TextField()

# Setting Plug Trace model
class SettingPlugTrace(models.Model):
    master_name = models.CharField(max_length=255)
    id_no = models.CharField(max_length=50)
    calibration_report_no = models.CharField(max_length=50)
    valid_upto = models.CharField(max_length=50)
    traceability = models.TextField()

# Setting Ring Trace model
class SettingRingTrace(models.Model):
    master_name = models.CharField(max_length=255)
    id_no = models.CharField(max_length=50)
    calibration_report_no = models.CharField(max_length=50)
    valid_upto = models.CharField(max_length=50)
    traceability = models.TextField()

# Setting Plug Master model
class SettingPlugMaster(models.Model):
    parameter_name = models.CharField(max_length=255)
    ref_size = models.CharField(max_length=50)
    nominal = models.CharField(max_length=50)

# Setting Ring Master model
class SettingRingMaster(models.Model):
    parameter_name = models.CharField(max_length=255)
    ref_size = models.CharField(max_length=50)
    nominal = models.CharField(max_length=50)

# Engineer Manager Details model
class EngineerManagerDetails(models.Model):
    calib_engineer = models.CharField(max_length=255)
    quality_manager = models.CharField(max_length=255)
    certificate_no = models.CharField(max_length=50)
