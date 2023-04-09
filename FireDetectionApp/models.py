from django.db import models

class FireInstance(models.Model):
    instance_no = models.IntegerField()
    instance_intensity = models.CharField(max_length=50)
    instance_time = models.CharField(max_length=50)
    instance_date = models.CharField(max_length=50)
    instance_address = models.CharField(max_length=100)