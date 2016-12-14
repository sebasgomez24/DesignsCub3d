from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^user/(\w+)/post_project/$', views.post_project, name='post_project'),
    url(r'^user/(\w+)/post_note/$', views.post_note, name='post_note'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.update_project, name='update_project'),
    url(r'^(?P<slug>[\w-]+)/update_note/$', views.update_note, name='update_note'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete_project, name='delete_project'),
    url(r'^(?P<slug>[\w-]+)/delete_note/$', views.delete_note, name='delete_note'),
    url(r'^user/(\w+)/update_profile/$', views.update_profile, name='update_profile'),
    url(r'^user/(\w+)/(?P<slug>[\w-]+)/comment/$', views.add_comment_to_note, name='add_comment_to_note'),
    url(r'^like_project/$', views.like_project, name='like_project'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^user/(\w+)/logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    
]

#add to bottom of file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT })
    ]