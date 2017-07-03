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

    url(regex=r'^choices_estado/(?P<estado>[\w]{2})/$',
        view=views.get_choices_cidades,
        name='get_choices_cidades'),

    url(regex=r'^ongs/$',
        view=views.RetornaONGs.as_view(),
        name='ongs-list'),

    url(regex=r'^ongs/(?P<pk>[\d]+)/$',
        view=views.RetornaONG.as_view(),
        name='ongs-detail'),

    url(regex=r'^ongs/(?P<estado>[\w]{2})/$',
        view=views.RetornaONGsEstado.as_view(),
        name='ongs-estado-list'),

    url(regex=r'^ongs/(?P<estado>[\w]{2})/(?P<cidade>[\w\-]+)/$',
        view=views.RetornaONGsCidade.as_view(),
        name='ongs-estado-cidade-list')
]
