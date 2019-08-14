# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pokemon
from .models import Trainer

admin.site.register(Pokemon)
admin.site.register(Trainer)