# Generated by Django 3.2.6 on 2021-12-17 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211217_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='hobbies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.hobbie'),
        ),
    ]
