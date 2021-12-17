# Generated by Django 3.2.6 on 2021-12-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211217_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='comments',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='main.Comment'),
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='photo',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='photo',
            field=models.ManyToManyField(blank=True, null=True, to='main.PhotoFile'),
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='video',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, to='main.VideoFile'),
        ),
    ]