# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
