# Generated by Django 2.1.4 on 2019-04-12 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20190411_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodohorario',
            name='horario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_periods', to='cms.Horario', verbose_name='Horario'),
        ),
    ]
