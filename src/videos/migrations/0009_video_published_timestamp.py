# Generated by Django 3.2.18 on 2023-02-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='published_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]