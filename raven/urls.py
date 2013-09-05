"""
Es nuestro fichero url.py que almacena todas las rutas
que debemos usar para ir a cada una de las secciones de nuestra web.
"""
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raven.views.home', name='home'),
    # url(r'^raven/', include('raven.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^index', 'raven.views.index', name='index'),
    url(r'^home', 'raven.views.home', name='home'),
    url(r'^about', 'raven.views.about', name='about'),
    url(r'^help', 'raven.views.help', name='help'),
    url(r'^contact', 'raven.views.contact', name='contact'),
   # url(r'^accounts/profile','users.views.profile'),
    url(r'^registro$','users.views.register'),
    url(r'^login/$', 'users.views.login_user'),
    url(r'^profile/$', 'users.views.update'),
    url(r'^borrar/(?P<post_id>\d+)/$', 'post.views.del_post'),
    url(r'^seguir/(?P<user_id>\d+)/$', 'users.views.follow'),
	url(r'^unfollow/(?P<user_id>\d+)/$', 'users.views.unfollow'),
	url(r'^perfil/(?P<user_id>\d+)/$', 'users.views.perfil'),
	url(r'^resp/(?P<post_id>\d+)/$', 'post.views.newreply'),
	url(r'^delrep/(?P<post_id>\d+)/$', 'post.views.delreply'),
	url(r'^deluser/$', 'users.views.deluser'),
    # Uncomment the next line to enable the admin:
    url(r'^logout/$','users.views.logout_view'),
    url(r'^admin/', include(admin.site.urls)),
    
)
