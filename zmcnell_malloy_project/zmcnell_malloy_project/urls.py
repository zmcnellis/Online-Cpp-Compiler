from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zmcnell_malloy_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'zmcnell_malloy_project.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^c_compiler/', include('c_compiler.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
