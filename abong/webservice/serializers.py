# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from webservice import models


class ONGSerializer(serializers.ModelSerializer):
    """
    Define a representação do model ONG.
    """
    cidade = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    estado = serializers.SlugRelatedField(slug_field='sigla', read_only=True)

    class Meta:
        """
        Definição dos campos que serão retornados pela API.
        """
        model = models.ONG
        fields = [
            'pk',
            'nome',
            'sigla',
            'descricao',
            'estado',
            'cidade',
            'imagem',
            'site',
            'banco',
            'agencia',
            'conta'
        ]
