# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from inputs.models import Input
from outputs.models import Output
from users.models   import User
admin.site.register(Input)
admin.site.register(Output)
# Register your models here.
