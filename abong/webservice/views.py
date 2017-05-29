# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers, viewsets
from webservice import models

class ONGSerializer(serializers.HyperlinkedModelSerializer):
    """
    Define a representação do model ONG.
    """
    class Meta:
        """
        Definição dos campos que serão retornados pela API.
        """
        model = models.ONG
        fields = '__all__'


class ONGViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o model ONG.
    """
    queryset = models.ONG.objects.all()
    serializer_class = ONGSerializer
    http_method_names = ['get']
