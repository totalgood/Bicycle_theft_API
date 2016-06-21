# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BicycleParkingPdx',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('objectid', models.FloatField(blank=True, null=True)),
                ('assetid', models.CharField(blank=True, max_length=15, null=True)),
                ('locationid', models.CharField(blank=True, max_length=15, null=True)),
                ('bpstyle', models.CharField(blank=True, max_length=6, null=True)),
                ('degx', models.FloatField(blank=True, null=True)),
                ('degy', models.FloatField(blank=True, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
                ('rack_score', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('bilinear_score', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'bicycle_parking_pdx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BicycleTheftsPdx',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('reported', models.DateTimeField(blank=True, null=True)),
                ('case_year', models.IntegerField(blank=True, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
                ('theft_score', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('theft_score_nbhood', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'bicycle_thefts_pdx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CornerImprovedPdx',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('geodb_oid', models.FloatField(blank=True, null=True)),
                ('objectid', models.FloatField(blank=True, null=True)),
                ('assetid', models.CharField(blank=True, max_length=15, null=True)),
                ('owner', models.CharField(blank=True, max_length=15, null=True)),
                ('maintresp', models.CharField(blank=True, max_length=15, null=True)),
                ('locationid', models.CharField(blank=True, max_length=15, null=True)),
                ('imagepath', models.CharField(blank=True, max_length=254, null=True)),
                ('extended', models.CharField(blank=True, max_length=1, null=True)),
                ('radius', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('material', models.CharField(blank=True, max_length=4, null=True)),
                ('histfeatur', models.CharField(blank=True, max_length=1, null=True)),
                ('drainagest', models.CharField(blank=True, max_length=254, null=True)),
                ('rampstyle', models.CharField(blank=True, max_length=254, null=True)),
                ('warningsty', models.CharField(blank=True, max_length=254, null=True)),
                ('shape_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('shape_len', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'corner_improved_pdx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CornerPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'corner_points',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NeighborhoodsPdx',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('objectid', models.FloatField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('commplan', models.CharField(blank=True, max_length=15, null=True)),
                ('shared', models.CharField(blank=True, max_length=1, null=True)),
                ('coalit', models.CharField(blank=True, max_length=10, null=True)),
                ('horz_vert', models.CharField(blank=True, max_length=4, null=True)),
                ('maplabel', models.CharField(blank=True, max_length=140, null=True)),
                ('id', models.FloatField(blank=True, null=True)),
                ('shape_star', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('shape_stle', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
                ('avg_rack_dist', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'neighborhoods_pdx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpatialRefSys',
            fields=[
                ('srid', models.IntegerField(primary_key=True, serialize=False)),
                ('auth_name', models.CharField(blank=True, max_length=256, null=True)),
                ('auth_srid', models.IntegerField(blank=True, null=True)),
                ('srtext', models.CharField(blank=True, max_length=2048, null=True)),
                ('proj4text', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'db_table': 'spatial_ref_sys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TheftGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', models.TextField(blank=True, null=True)),
                ('num_racks', models.IntegerField(blank=True, null=True)),
                ('num_corners', models.IntegerField(blank=True, null=True)),
                ('num_thefts', models.IntegerField(blank=True, null=True)),
                ('grid_score', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('point_geom', models.TextField(blank=True, null=True)),
                ('test_geom', models.TextField(blank=True, null=True)),
                ('valid_data', models.IntegerField(blank=True, null=True)),
                ('degx', models.FloatField(blank=True, null=True)),
                ('degy', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'theft_grid',
                'managed': False,
            },
        ),
    ]