# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
#
# from django.shortcuts import render
#
# # Create your views here.

from rest_framework import viewsets

from .serializers import CardSerializer
from .models import Card

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
