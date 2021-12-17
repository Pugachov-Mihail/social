# Generated by Django 3.2.6 on 2021-12-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211217_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbie',
            name='discription',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='hobbies',
            field=models.ManyToManyField(blank=True, null=True, related_name='hobbie', to='main.Hobbie'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.ManyToManyField(blank=True, null=True, related_name='photos', to='main.PhotoFile'),
        ),
    ]
