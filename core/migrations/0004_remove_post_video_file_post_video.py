# Generated by Django 4.2.4 on 2023-08-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_video_post_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video_file',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
