from django.db import models

# Create your models here.
class ToServices(models.Model):
    ser_id = models.BigAutoField(primary_key=True)
    number_to = models.IntegerField()
    type_work = models.CharField(max_length=255)
    datetime = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'to_services'


class ToRepairs(models.Model):
    rep_id = models.BigAutoField(primary_key=True)
    name_mtr = models.CharField(max_length=255)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'to_repairs'


class ToShedule(models.Model):
    shed_id = models.BigAutoField(primary_key=True)
    system = models.CharField(max_length=255)
    quantity = models.IntegerField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'to_shedule'