# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
#
# from django.shortcuts import render
#
# # Create your views here.

from rest_framework import viewsets

from .serializers import CardSerializer, ListSerializer
from .models import Card, List

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.order_by("order")
    serializer_class = ListSerializer
