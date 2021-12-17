# Generated by Django 3.2.6 on 2021-12-17 19:38

from django.conf import settings
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211216_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='hobbies',
        ),
        migrations.AddField(
            model_name='hobbie',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photofile',
            name='url',
            field=models.ImageField(upload_to=main.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='url',
            field=models.FileField(upload_to='photo/%Y/%m/%d/%s'),
        ),
    ]
