# Generated by Django 4.2.15 on 2024-11-21 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0008_ordentrabajo_estadoordentrabajo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordentrabajo',
            name='esPagoTotal',
        ),
        migrations.RemoveField(
            model_name='ordentrabajo',
            name='estadoDelPago',
        ),
    ]