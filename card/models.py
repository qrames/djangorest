# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    order = models.PositiveIntegerField()
    list = models.ForeignKey(List, related_name="cards", on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title
