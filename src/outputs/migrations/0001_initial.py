# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-23 22:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import outputs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inputs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('clean_layer', models.CharField(max_length=500)),
                ('spd_tol', models.IntegerField()),
                ('buffr', models.IntegerField()),
                ('n_freq', models.IntegerField()),
                ('n_points', models.IntegerField()),
                ('d_gps', models.FileField(blank=True, upload_to=outputs.models.output_directory_path)),
                ('d_res', models.FileField(blank=True, upload_to=outputs.models.output_directory_path)),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputs.Input')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
