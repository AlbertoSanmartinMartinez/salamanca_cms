# Generated by Django 2.1.4 on 2019-03-27 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0025_auto_20190327_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodohorario',
            name='dia',
            field=models.CharField(blank=True, choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], default='Lunes', max_length=9, verbose_name='Día'),
        ),
    ]
