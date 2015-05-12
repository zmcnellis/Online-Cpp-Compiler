from django.conf.urls import patterns, url
from c_compiler import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    )

