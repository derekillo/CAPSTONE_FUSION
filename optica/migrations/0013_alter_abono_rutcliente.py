# Generated by Django 4.2.15 on 2024-11-25 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optica', '0012_remove_certificado_rutadministrador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abono',
            name='rutCliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='optica.cliente', verbose_name='RUN Cliente'),
        ),
    ]