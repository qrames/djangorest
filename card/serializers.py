# api/serializers.py


from rest_framework import serializers
from blogengine import models


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        # Vous pouvez ajouter un fields pour filtrer les
        # champs du modèle à sérialiser
        fields = ('title', 'content')
