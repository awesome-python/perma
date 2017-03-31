from django.conf.urls import url
from diff import views

guid_pattern = r'(?P<guid>[a-zA-Z0-9\-]{8,11})'

urlpatterns = [
    #url(r'(?P<guid>.+)/diff/?$', views.diff_entry, name='diff_entry'),
    url(r'^%s/diff/?$' % guid_pattern, views.diff_entry, name='diff_entry'),
    #url('diff/?$', views.diff_entry, name='diff_entry'),
]