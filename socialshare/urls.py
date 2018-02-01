from django.conf.urls import url

from socialshare.views import share_email

app_name = 'socialshare'

urlpatterns = [
    url(r'^send-friend/$', share_email, name='social-share-email'),
]
