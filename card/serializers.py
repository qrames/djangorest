# -*- coding: utf-8 -*-
# api/serializers.py


from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        # Vous pouvez ajouter un fields pour filtrer les
        # champs du modèle à sérialiser
        fields = ('id', 'title', 'content')
