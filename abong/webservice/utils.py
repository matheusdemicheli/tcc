# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import collections
from rest_framework.reverse import reverse
from webservice import models


def get_urls(request, format=None):
    """
    Retorna um índice de URLs do Web Service.
    """
    urls = {
        'ongs': reverse('ongs-list', request=request, format=format),
        'urls_estados': reverse('urls-estados-list', request=request, format=format),
        'urls_cidades': reverse('urls-cidades-list', request=request, format=format),
    }
    return collections.OrderedDict(sorted(urls.items()))


def get_urls_estados(request, format=None):
    """
    Retorna todas as possíveis URLs para acesso às ONGs por estado.
    """
    urls = collections.OrderedDict()
    estados = models.Estado.objects.all()
    for estado in estados.order_by('sigla'):
        chave = 'ongs-%s' % estado.sigla
        url = reverse(
            'ongs-estado-list',
            args=[estado.sigla],
            request=request,
            format=format,

        )
        urls[chave] = url
    return urls


def get_urls_cidades(request, format=None):
    """
    Retorna todas as possíveis URLs para acesso às ONGs por cidade.
    """
    urls = collections.OrderedDict()
    cidades = models.Cidade.objects.all().select_related('estado')
    for cidade in cidades.order_by('nome'):
        chave = 'ongs-%s' % cidade.slug
        url = reverse(
            'ongs-estado-cidade-list',
            args=[cidade.estado.sigla, cidade.slug],
            request=request,
            format=format,
        )
        urls[chave] = url
    return urls
