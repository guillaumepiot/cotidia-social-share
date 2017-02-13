from django.conf.urls import url

from socialshare.views import share_email


urlpatterns = [
    url(r'^send-friend/$', share_email, name='social-share-email'),
]
