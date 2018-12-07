# -*- coding: utf-8 -*-
# api/serializers.py


from rest_framework import serializers
from .models import Card, List

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        # Vous pouvez ajouter un fields pour filtrer les
        # champs du modèle à sérialiser
        fields = ('id', 'title', 'content')


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = '__all__'
