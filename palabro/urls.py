from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.init, name='init'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^language/new/$', views.language_new, name='language_new'),
    url(r'^language/list/$', views.language_list, name='language_list'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
]