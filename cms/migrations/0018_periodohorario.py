# Generated by Django 2.1.4 on 2019-03-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20190317_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodoHorario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.TimeField(blank=True, verbose_name='Apertura')),
                ('fin', models.TimeField(blank=True, verbose_name='Cierre')),
            ],
            options={
                'verbose_name': 'PeriodoHorario',
                'verbose_name_plural': 'PeriodosHorario',
            },
        ),
    ]
