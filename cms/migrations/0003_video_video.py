# Generated by Django 2.1.4 on 2019-03-04 09:34

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_remove_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True, verbose_name='Video Url'),
        ),
    ]
