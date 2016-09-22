from django.conf.urls import patterns, include, url
import sys
from django.contrib import admin
from fibonacci import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.fibonacci_home , name='fibonacci_home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^fibonacci-series/(?P<nterms>[A-Za-z0-9+/=]+)/$', views.fibonacci , name='fibonacci'),

    url(r'^fibonacci/$',views.fibonacci, name='fibonacci'),
)
