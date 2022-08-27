from django.db import models

# Create your models here.
class RefEquip(models.Model):
    id_eq = models.BigAutoField(primary_key=True)
    id_sys = models.SmallIntegerField()
    uid_eq = models.UUIDField()
    desc_eq = models.CharField(max_length=255)
    count_eq = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'ref_equip'


class RefObj(models.Model):
    id_bur = models.BigAutoField(primary_key=True)
    uid_bur = models.UUIDField()
    desc_bur = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ref_obj'


class RefSys(models.Model):
    id_sys = models.BigAutoField(primary_key=True)
    uid_sys = models.UUIDField()
    desc_sys = models.CharField(max_length=255)
    id_obj = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ref_sys'