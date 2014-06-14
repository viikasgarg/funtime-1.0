from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'sudokusolver.views.home', name='sudokusolver.home'),
     url(r'^play/$', 'sudokusolver.views.play', name='sudokusolver.play.home'),
     url(r'^play/(?P<level>\w*)$', 'sudokusolver.views.play', name='sudokusolver.play'),
)
