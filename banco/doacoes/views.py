#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def doacoes(request):
    """
    View para a página de doações.
    """
    return HttpResponse('olá')
