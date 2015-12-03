from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       # Examples:
                       url(r'^$',
                           'guesscolor.views.home',
                           name='guesscolor.home'),
                       )
