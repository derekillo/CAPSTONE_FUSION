# Generated by Django 4.2.15 on 2024-10-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0003_alter_receta_rutadministrador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordentrabajo',
            old_name='colorCerca',
            new_name='colorCristalCerca',
        ),
        migrations.RenameField(
            model_name='ordentrabajo',
            old_name='colorLejos',
            new_name='colorCristalLejos',
        ),
        migrations.RemoveField(
            model_name='ordentrabajo',
            name='creacionOrdenTrabajo',
        ),
        migrations.RemoveField(
            model_name='ordentrabajo',
            name='valorOrdenTrabajo',
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='adicionCercaOd',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Adición Cerca OD'),
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='adicionCercaOi',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Adición Cerca OI'),
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='adicionLejosOd',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Adición Lejos OD'),
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='adicionLejosOi',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Adición Lejos OI'),
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='numeroOrdenTrabajo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total (Lejos)'),
        ),
    ]
