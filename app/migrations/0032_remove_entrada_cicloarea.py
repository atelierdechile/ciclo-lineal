# Generated by Django 4.0.6 on 2022-07-25 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_rename_area_registrotrabajador_id_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='cicloArea',
        ),
    ]