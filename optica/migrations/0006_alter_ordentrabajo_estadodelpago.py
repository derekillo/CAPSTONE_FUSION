# Generated by Django 4.2.15 on 2024-11-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0005_ordentrabajo_estadodelpago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordentrabajo',
            name='estadoDelPago',
            field=models.CharField(default=11, max_length=20, verbose_name='Estado del Pago'),
            preserve_default=False,
        ),
    ]
