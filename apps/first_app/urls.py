from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/$', views.process),
    url(r'^(?P<id>\d+)/remove/$', views.remove),
    url(r'^dont/$', views.dont),
    url(r'^(?P<id>\d+)/destroy/$', views.destroy)
]