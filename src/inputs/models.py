# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from datetime import datetime

def input_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<user.id>/input_<id>/<filename>
	# obtenido de https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
	return 'uploads/user_0/gbd/%s/%s' % (datetime.today().strftime('%Y%m%d'), filename)

#def layer_directory_path(instance,filename):
	# obtenido de https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
#	return 'user_{0}/input_{1}/%Y_%m_%d/lyr/{2}'.format('0',instance.id, filename)

# Create your models here.
class Input(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	red_vial_layer = models.CharField(blank=False, max_length = 50)
	GPS_layer = models.CharField(blank=False, max_length = 50)
	gbd = models.FileField(blank=False, upload_to=input_directory_path)
	description = models.TextField(default='')
	gbd_root = models.CharField(max_length = 500)
	metrica = models.CharField(max_length =500, blank=False)

	def __str__(self):
		return "%s %s" % (self.GPS_layer, self.red_vial_layer)
