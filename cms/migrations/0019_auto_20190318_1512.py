# Generated by Django 2.1.4 on 2019-03-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_periodohorario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodohorario',
            options={'verbose_name': 'Horario Plus', 'verbose_name_plural': 'Horarios Plus'},
        ),
        migrations.AddField(
            model_name='periodohorario',
            name='dia',
            field=models.BooleanField(blank=True, default=None, verbose_name='Día'),
            preserve_default=False,
        ),
    ]
