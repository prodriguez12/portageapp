# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-23 22:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import inputs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_vial_layer', models.CharField(max_length=50)),
                ('GPS_layer', models.CharField(max_length=50)),
                ('gbd', models.FileField(upload_to=inputs.models.input_directory_path)),
                ('description', models.TextField(default='')),
                ('gbd_root', models.CharField(max_length=500)),
                ('metrica', models.CharField(max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
