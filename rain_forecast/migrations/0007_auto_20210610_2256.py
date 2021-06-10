# Generated by Django 3.1.7 on 2021-06-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rain_forecast', '0006_door_magneticswitch_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='location',
        ),
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
        migrations.RemoveField(
            model_name='device',
            name='register_user',
        ),
        migrations.AddField(
            model_name='device',
            name='aio_key',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='topic_name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]