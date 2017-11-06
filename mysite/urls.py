from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('palabro.urls')),
]
