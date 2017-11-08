from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/profile/$', views.profile, name='profile'),
    url(r'^user/native_language/$', views.set_native_language, name='native_language'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^language/new/$', views.language_new, name='language_new'),
    url(r'^language/list/$', views.language_list, name='language_list'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
]
