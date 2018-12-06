# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Card
# Register your models here.

class CardAdmin(admin.ModelAdmin):
    model = Card


admin.site.register(Card)
