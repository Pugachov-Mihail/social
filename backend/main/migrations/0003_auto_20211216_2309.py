# Generated by Django 3.2.6 on 2021-12-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211216_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photofile',
            name='url',
            field=models.ImageField(upload_to='photo/<function user_directory_path at 0x000001F64EA2D160>/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='url',
            field=models.FileField(upload_to='photo/%Y/%m/%d/<function user_directory_path at 0x000001F64EA2D160>'),
        ),
    ]
