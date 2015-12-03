from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#import settings
import autocomplete_light
# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'main.views.home', name='main.home'),
                       # url(r'^funtime/', include('funtime.foo.urls')),
                       #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       url(r'^autocomplete/',
                           include('autocomplete_light.urls')),
                       url(r'^main/', include('main.urls')),
                       url(r'^sudokusolver/', include('sudokusolver.urls')),
                       url(r'^brainteaser/', include('brainteaser.urls')),
                       url(r'^guesscolor/', include('guesscolor.urls')),
                       url(r'^calculator/', include('calculator.urls')),
                       url(r'^numkundli/', include('numkundli.urls')),
                       url(r'^dictionary/', include('dictionary.urls')),
                       url(r'^2048/', include('2048.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
