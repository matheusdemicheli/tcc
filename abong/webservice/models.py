# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


class Estado(models.Model):
    """
    Estados brasileiros.
    """

    sigla = models.CharField(max_length=2)

    nome = models.CharField(max_length=50)

    def __unicode__(self):
        """
        Retorna a representação do objeto.
        """
        return u'%s - %s' % (self.sigla.upper(), self.nome)


class Cidade(models.Model):
    """
    Cidades brasileiras.
    """

    estado = models.ForeignKey(Estado)

    nome = models.CharField(max_length=100)

    slug = models.CharField(max_length=100, editable=False)

    def save(self, *args, **kwargs):
        """
        Sobrescrito para criar o slug antes de salvar.
        """
        self.slug = slugify(self.nome)
        return super(Cidade, self).save(*args, **kwargs)

    def __unicode__(self):
        """
        Retorna a representação do objeto.
        """
        return u'%s - %s' % (self.nome, self.estado.sigla)


class ONG(models.Model):
    """
    Abstração de uma ONG.
    """

    nome = models.CharField(max_length=70)

    sigla = models.CharField(max_length=15, null=True, blank=True)

    descricao = models.TextField()

    estado = models.ForeignKey(Estado)

    cidade = models.ForeignKey(Cidade)

    imagem = models.ImageField()

    site = models.CharField(max_length=100, null=True, blank=True)

    banco = models.PositiveSmallIntegerField()

    agencia = models.PositiveSmallIntegerField()

    conta = models.PositiveSmallIntegerField()

    def __unicode__(self):
        """
        Retorna a representação do objeto.
        """
        return self.nome
