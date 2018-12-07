# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Card, List
# Register your models here.

class CardAdmin(admin.ModelAdmin):
    model = Card


class ListAdmin(admin.ModelAdmin):
    model = List


admin.site.register(Card)
admin.site.register(List)
