# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webservice import models, serializers, utils


@api_view(['GET'])
def api_root(request, format=None):
    """
    URLs disponíveis para acesso.
    """
    return Response(utils.get_urls(request=request, format=format))


@api_view(['GET'])
def urls_estados(request, format=None):
    """
    URLs de estados disponíveis para acesso.
    Formato da URL: /api/ongs/{estado}/
    """
    return Response(utils.get_urls_estados(request=request, format=format))


@api_view(['GET'])
def urls_cidades(request, format=None):
    """
    URLs de cidades disponíveis para acesso.
    Formato da URL: /api/ongs/{estado}/{cidade}/
    """
    return Response(utils.get_urls_cidades(request=request, format=format))


class ONGDetail(generics.RetrieveAPIView):
    """
    Informações de uma ONG.
    """
    serializer_class = serializers.ONGSerializer
    queryset = models.ONG.objects.all()


class ONGList(generics.ListAPIView):
    """
    Coleção de informações de uma ou mais ONGs.
    """
    serializer_class = serializers.ONGSerializer
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


class ONGEstadoCidadeList(ONGEstadoList):
    """
    Retorna uma lista de ONGs, filtrada por estado e cidade.
    """

    def get_queryset(self):
        """
        Sobrescrito para filtrar o queryset por estado e cidade.
        """
        queryset = super(ONGEstadoCidadeList, self).get_queryset()
        return queryset.filter(cidade__slug=self.kwargs['cidade'])
