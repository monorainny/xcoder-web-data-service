from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebDataRestService.views.home', name='home'),
    # url(r'^WebDataRestService/', include('WebDataRestService.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'DbService.views.index', name='index'),
    
    url(r'^query/execute/$', 'DbService.views.executeQuery', name='index'),
    url(r'^query/update/$', 'DbService.views.updateQuery', name='index'),
)
