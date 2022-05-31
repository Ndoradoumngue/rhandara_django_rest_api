# Generated by Django 3.1.13 on 2021-08-02 11:13

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude_coordinate', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude_coordinate', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=5000, null=True, unique=True)),
                ('added_on_date_time', models.DateTimeField(auto_now_add=True)),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.town')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=5000, null=True, unique=True)),
                ('added_on_date_time', models.DateTimeField(auto_now_add=True)),
                ('point_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_point_one', to='main_app.area')),
                ('point_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_point_two', to='main_app.area')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_point_latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('starting_point_longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('arriving_point_latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('arriving_point_longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField()),
                ('is_new_request', models.BooleanField(default=True)),
                ('request_accepted', models.BooleanField(default=False)),
                ('request_accepted_on_date_time', models.DateTimeField(blank=True, null=True)),
                ('trip_started', models.BooleanField(default=False)),
                ('trip_started_on_date_time', models.DateTimeField(blank=True, null=True)),
                ('trip_finished', models.BooleanField(default=False)),
                ('trip_finished_on_date_time', models.DateTimeField(blank=True, null=True)),
                ('trip_cancelled', models.BooleanField(default=False)),
                ('trip_cancelled_on_date_time', models.DateTimeField(blank=True, null=True)),
                ('client_trip_rating', models.IntegerField(default=0)),
                ('driver_trip_rating', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=5000, null=True, unique=True)),
                ('request_started_on_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('rating', models.IntegerField(default=5)),
                ('number_of_ratings', models.IntegerField(default=0)),
                ('number_of_raters', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=5000, null=True, unique=True)),
                ('added_on_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=5000, null=True, unique=True)),
                ('added_on_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='youtube_profile_link',
        ),
        migrations.AddField(
            model_name='systemuser',
            name='current_area_location',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='is_available_to_driver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='is_car_driver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='is_motorbike_driver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='number_of_raters',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_country', to='main_app.country'),
        ),
        migrations.DeleteModel(
            name='Rapport',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_added_by', to='main_app.systemuser'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.vehiclebrand'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_owner', to='main_app.systemuser'),
        ),
        migrations.AddField(
            model_name='trip',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_by_client', to='main_app.systemuser'),
        ),
        migrations.AddField(
            model_name='trip',
            name='request_accepted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_picked_by_driver', to='main_app.systemuser'),
        ),
        migrations.AddField(
            model_name='trip',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.route'),
        ),
        migrations.AddField(
            model_name='trip',
            name='starting_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.area'),
        ),
    ]
