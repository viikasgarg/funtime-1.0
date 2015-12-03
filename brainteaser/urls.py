from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       # Examples:
                       url(r'^$',
                           'brainteaser.views.home',
                           name='brainteaser.home'),
                       )
