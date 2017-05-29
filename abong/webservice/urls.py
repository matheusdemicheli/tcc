#-*- coding utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers
from webservice import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ongs', views.ONGViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
