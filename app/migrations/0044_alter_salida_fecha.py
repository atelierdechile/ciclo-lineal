# Generated by Django 4.0.6 on 2022-08-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_alter_entrada_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]