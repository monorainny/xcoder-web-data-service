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
    
    url(r'^$', 'LogService.views.index', name='index'),
    
    url(r'^top/', 'LogService.views.top', name='top'),
    url(r'^left/', 'LogService.views.left', name='left'),
    url(r'^main/', 'LogService.views.main', name='main'),
    
    url(r'^jqgrid_main/', 'LogService.views.jqgrid_main', name='jqgrid_main'),
    url(r'^data_load/', 'LogService.views.data_load', name='data_load'),
    
    url(r'^DbQuery/', 'DbService.views.index', name='index'),
    
    url(r'^query/execute/$', 'DbService.views.executeQuery', name='index'),
    url(r'^query/update/$', 'DbService.views.updateQuery', name='index'),
    
    #url(r'^login/$', 'LogService.views.login_page'),
    #url(r'^login/action/$', 'LogService.views.login_check'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'LogService.views.logout_page'),
    url(r'^accounts/regist/$', 'LogService.views.accounts_regist'),
    url(r'^accounts/regist_action/$', 'LogService.views.accounts_regist_action'),
    url(r'^accounts/info/$', 'LogService.views.accounts_info'),
    url(r'^accounts/info_modify/$', 'LogService.views.accounts_info_modify'),
    
    url(r'^main_refresh/$', 'LogService.views.main_refresh'),
)
