# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers, generics, filters
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


class ONGDetail(generics.RetrieveAPIView):
    """
    Retorna uma coleção de informações de uma ONG.
    """
    serializer_class = ONGSerializer
    queryset = models.ONG.objects.all()


class ONGList(generics.ListAPIView):
    """
    Retorna uma coleção de informações uma ou mais ONGs.
    """
    serializer_class = ONGSerializer
    queryset = models.ONG.objects.all()
    filter_backends = (
        filters.SearchFilter,
    )
    ordering = ('nome',)
    search_fields = ('nome', 'sigla')

    def get_queryset(self):
        """
        Sobrescrito para aplicar filtros.
        """
        queryset = self.queryset.all()
        campos_ordenacao = self.request.query_params.getlist('ordem')

        if 'estado' in campos_ordenacao:
            indice = campos_ordenacao.index('estado')
            campos_ordenacao.pop(indice)
            campos_ordenacao.insert(indice, 'estado__sigla')

        if 'cidade' in campos_ordenacao:
            indice = campos_ordenacao.index('cidade')
            campos_ordenacao.pop(indice)
            campos_ordenacao.insert(indice, 'cidade__slug')

        return queryset.order_by(*campos_ordenacao)


class ONGEstadoList(ONGList):
    """
    Retorna uma lista de ONGs, filtrada por estado.
    """

    def get_queryset(self):
        """
        Sobrescrito para filtrar o queryset por estado.
        """
        queryset = super(ONGEstadoList, self).get_queryset()
        return queryset.filter(estado__sigla=self.kwargs['estado'])


class ONGEstadoCidadeList(ONGList):
    """
    Retorna uma lista de ONGs, filtrada por estado e cidade.
    """

    def get_queryset(self):
        """
        Sobrescrito para filtrar o queryset por estado e cidade.
        """
        queryset = super(ONGEstadoList, self).get_queryset()
        return queryset.filter(
            estado__sigla=self.kwargs['estado'],
            cidade__slug=self.kwargs['cidade']
        )
