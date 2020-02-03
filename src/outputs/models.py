# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from inputs.models import Input

# Create your models here.
def output_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/output_<id>/<filename>
    # obtenido de https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    return 'user_{0}/output_{1}/%Y_%m_%d/{2}'.format(instance.user.id, instance.id, filename)

class Output(models.Model):
	origin = models.ForeignKey(Input, on_delete=models.CASCADE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	start = models.DateTimeField(auto_now=False,auto_now_add=False)
	finish = models.DateTimeField(auto_now=False,auto_now_add=False)
	clean_layer = models.CharField(max_length = 500, null=False, blank=False)
	spd_tol = models.IntegerField()
	buffr = models.IntegerField()
	n_freq = models.IntegerField()
	n_points = models.IntegerField()
	d_gps = models.FileField(blank=True, upload_to=output_directory_path)
	d_res = models.FileField(blank=True, upload_to=output_directory_path)

	def __str__(self):
		return self.clean_layer




	#def save_file(self):
	#	f = open('pages/salida.txt')
	#	file = File(f)
	#	self.root.save(str(self.id)+"salida.txt", file)
	#	f.close()
