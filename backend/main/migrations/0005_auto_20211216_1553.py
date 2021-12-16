# Generated by Django 3.2.6 on 2021-12-16 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211216_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photofile',
            name='url',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/<function user_path at 0x000001ED8D1720D0>'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='hobbies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.hobbie'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.photofile'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.videofile'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='url',
            field=models.FileField(upload_to='photo/%Y/%m/%d/<function user_path at 0x000001ED8D1720D0>'),
        ),
    ]
