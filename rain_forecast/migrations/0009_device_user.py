# Generated by Django 3.1.7 on 2021-08-01 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rain_forecast', '0008_auto_20210625_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rain_forecast.user'),
        ),
    ]
