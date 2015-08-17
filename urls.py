from django.conf import settings
# from django.conf.urls.defaults import *  
from django.conf.urls import patterns, url, include
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# import xadmin
# xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^www/', include('www.foo.urls')),

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    # (r'^tinymce/', include('tinymce.urls')),
    # url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^$', 'engine.post.home' ),
    url(r'^project-list/$', 'engine.project.project_list', name="project_list"),
    url(r'^project/(\d+)$', 'engine.project.project', name="project"),
    url(r'^(\d+)$', 'engine.post.task', name="task"),
    url(r'^create-task/$', 'engine.post.create_task' ),
    # url(r'^img-upload/$', 'engine.post.img_upload' ),
    # url(r'^project-thumbnail-upload/$', 'engine.project.project_thumbnail_upload' ),
    # url(r'^brand-logo-upload/$', 'engine.brand.brand_logo_upload' ),
    url(r'^edit-task/$', 'engine.post.edit_task' ),
    url(r'^save-task/$', 'engine.post.save_task' ),
    url(r'^del-task/$', 'engine.post.del_task' ),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns