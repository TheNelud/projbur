# Generated by Django 4.1 on 2022-08-27 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projbur_app', '0003_alter_refequip_options_alter_refobj_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refequip',
            old_name='id',
            new_name='id_eq',
        ),
        migrations.AlterModelTable(
            name='refequip',
            table='ref_equip',
        ),
    ]
