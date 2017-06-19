#-*- coding utf-8 -*-

from django.conf.urls import include, url
from webservice import views


urlpatterns = [
    url(regex=r'^$',
        view=views.api_root,
        name='api-root'),

    url(regex=r'^urls/estados/$',
        view=views.urls_estados,
        name='urls-estados-list'),

    url(regex=r'^urls/cidades/$',
        view=views.urls_cidades,
        name='urls-cidades-list'),

    url(regex=r'^ongs/$',
        view=views.ONGList.as_view(),
        name='ongs-list'),

    url(regex=r'^ongs/detail/(?P<pk>[\w]+)/$',
        view=views.ONGDetail.as_view(),
        name='ongs-detail'),

    url(regex=r'^ongs/(?P<estado>[\w]+)/$',
        view=views.ONGEstadoList.as_view(),
        name='ongs-estado-list'),

    url(regex=r'^ongs/(?P<estado>[\w]+)/(?P<cidade>[\w\-]+)/$',
        view=views.ONGEstadoCidadeList.as_view(),
        name='ongs-estado-cidade-list')
]
