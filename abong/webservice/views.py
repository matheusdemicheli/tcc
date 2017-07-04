# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webservice import models, serializers, utils
from django.shortcuts import render_to_response

def site(request):
    """
    Retorna a página inicial do site da Abong.
    """
    return render_to_response('abong.html')


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


@api_view(['GET'])
def get_choices_cidades(request, estado):
    """
    Retorna os choices para determinado estado.
    """
    cidades = models.Cidade.objects.filter(estado__sigla=estado)
    return Response(cidades.values_list('slug', 'nome'))


class RetornaONG(generics.RetrieveAPIView):
    """
    Informações de uma ONG.
    """
    serializer_class = serializers.ONGSerializer
    queryset = models.ONG.objects.all()


class RetornaONGs(generics.ListAPIView):
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

    def get_queryset(self, queryset=None):
        """
        Sobrescrito para aplicar filtros.
        """
        if queryset is None:
            queryset = self.queryset.all()

        campos_ordenacao = self.request.query_params.getlist('ordem') or ['pk']

        if 'estado' in campos_ordenacao:
            indice = campos_ordenacao.index('estado')
            campos_ordenacao.pop(indice)
            campos_ordenacao.insert(indice, 'estado__sigla')

        if 'cidade' in campos_ordenacao:
            indice = campos_ordenacao.index('cidade')
            campos_ordenacao.pop(indice)
            campos_ordenacao.insert(indice, 'cidade__slug')

        pesquisa = self.request.query_params.get('pesquisa')
        if pesquisa:
            queryset = (
                queryset.filter(nome__icontains=pesquisa) |
                queryset.filter(sigla__icontains=pesquisa)
            )

        pagina = int(self.request.query_params.get('pagina') or '1')

        itens_por_pagina = \
            int(self.request.query_params.get('itens-por-pagina') or '15')

        limite_superior = pagina * itens_por_pagina
        limite_inferior = limite_superior - itens_por_pagina

        queryset = queryset.order_by(*campos_ordenacao)
        queryset = queryset[limite_inferior:limite_superior]
        return models.ONG.objects.filter(
            pk__in=queryset.values_list('pk', flat=True)
        ).order_by(*campos_ordenacao)


class RetornaONGsEstado(RetornaONGs):
    """
    Retorna uma lista de ONGs, filtrada por estado.
    """

    def get_queryset(self, queryset=None):
        """
        Sobrescrito para filtrar o queryset por estado.
        """
        if queryset is None:
            queryset = self.queryset.all()

        queryset = queryset.filter(estado__sigla=self.kwargs['estado'])
        return super(RetornaONGsEstado, self).get_queryset(queryset)


class RetornaONGsCidade(RetornaONGsEstado):
    """
    Retorna uma lista de ONGs, filtrada por estado e cidade.
    """

    def get_queryset(self, queryset=None):
        """
        Sobrescrito para filtrar o queryset por estado e cidade.
        """
        if queryset is None:
            queryset = self.queryset.all()

        queryset = queryset.filter(cidade__slug=self.kwargs['cidade'])
        return super(RetornaONGsCidade, self).get_queryset(queryset)
