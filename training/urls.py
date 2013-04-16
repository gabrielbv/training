from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'training.views.home', name='home'),
    # url(r'^training/', include('training.foo.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),

    #handler500 = 'mysite.views.my_custom_error_view'
    
    #handler404 = 'mysite.views.my_custom_404_view'
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    #url(r'^admin/', include(admin.site.urls)),
)
