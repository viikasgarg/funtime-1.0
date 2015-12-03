from django.conf.urls import patterns, url
from .views import KundliFormView

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$',
                           KundliFormView.as_view(),
                           name='numkundli.home'),

                       )
