# Generated by Django 2.1.4 on 2019-04-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodohorario',
            name='fin',
            field=models.TimeField(default='20:00', verbose_name='Cierre'),
        ),
        migrations.AlterField(
            model_name='periodohorario',
            name='inicio',
            field=models.TimeField(default='09:00', verbose_name='Apertura'),
        ),
    ]
