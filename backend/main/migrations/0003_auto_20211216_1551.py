# Generated by Django 3.2.6 on 2021-12-16 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211216_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photofile',
            name='url',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/<function user_path at 0x000002826166FF70>'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='comments',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.comment'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='hobbies',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.hobbie'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.photofile'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='video',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.videofile'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='url',
            field=models.FileField(upload_to='photo/%Y/%m/%d/<function user_path at 0x000002826166FF70>'),
        ),
    ]