# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#My Custom Models
class Trainer(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name   
