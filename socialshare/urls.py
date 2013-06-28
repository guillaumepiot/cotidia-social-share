from django.conf.urls.defaults import *

urlpatterns = patterns('socialshare.views',
    url(r'^send-friend/$', 'share_email', name='social-share-email'),

)
