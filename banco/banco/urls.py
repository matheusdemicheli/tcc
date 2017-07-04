from django.conf.urls import include, url
from doacoes.views import doacoes, servico
#from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'banco.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     #url(r'^admin/', include(admin.site.urls)),
#     url(r'^/doacoes/$', 'doacoes.views.doacoes' )
# )


urlpatterns = [
    url(r'^$', servico),
    url(r'^doacoes/$', doacoes, name='doacoes'),
]
