from django.conf.urls import url, patterns

urlpatterns = patterns('socialshare.views',
    url(r'^send-friend/$', 'share_email', name='social-share-email'),
)
