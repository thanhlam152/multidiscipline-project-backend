# Generated by Django 3.1.7 on 2021-05-20 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rain_forecast', '0005_device_register_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagneticSwitch',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='rain_forecast.device')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField()),
                ('data', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rain_forecast.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('DR', 'Main door'), ('WD', 'Window')], default='DR', max_length=2)),
                ('status', models.CharField(choices=[('CL', 'Closed'), ('OP', 'Open')], default='CL', max_length=2)),
                ('switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rain_forecast.magneticswitch')),
            ],
        ),
    ]
