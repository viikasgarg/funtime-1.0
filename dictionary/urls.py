from django.conf.urls import patterns, url
from .views import DictionaryView

urlpatterns = patterns('',
    # Examples:
     url(r'^$', DictionaryView.as_view(), name='dictionary.home'),

)
