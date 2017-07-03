#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response


# Create your views here.
def doacoes(request):
    """
    View para a página de doações.
    """
    return render_to_response('doacao.html', {})
