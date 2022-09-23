# Generated by Django 3.2.13 on 2022-07-05 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForecastPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forecast_period', models.CharField(max_length=10)),
                ('forecast_this_cycle', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_item', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sbe_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sbe_2', models.CharField(max_length=15, null=True)),
                ('forecast_this_cycle', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuarterPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter_period', models.CharField(max_length=8, null=True)),
                ('forecast_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.forecastperiod')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('program_manager', models.CharField(max_length=100)),
                ('forecast_this_cycle', models.BooleanField(default=True)),
                ('internal_ord_list', models.CharField(default='', max_length=1000)),
                ('sbe_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.sbe_2')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.FloatField()),
                ('comment', models.CharField(max_length=1000)),
                ('line_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.lineitem')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.program')),
                ('quarter_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.quarterperiod')),
            ],
        ),
    ]