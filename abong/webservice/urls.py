#-*- coding utf-8 -*-

from django.conf.urls import include, url
from webservice import views


urlpatterns = [
    url(r'^ongs/$', views.ONGList.as_view()),
    url(r'^ongs/(?P<pk>[\w]+)/$', views.ONGDetail.as_view()),
    url(r'^ongs/(?P<estado>[\w]+)/$', views.ONGEstadoList.as_view()),
    url(r'^ongs/(?P<estado>[\w]+)/(?P<cidade>[\w\-]+)/$', views.ONGEstadoCidadeList.as_view())
]
