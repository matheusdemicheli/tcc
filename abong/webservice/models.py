# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ONG(models.Model):
    """
    Abstração de uma ONG.
    """

    nome = models.CharField(max_length=50)

    sigla = models.CharField(max_length=10)

    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome
