from django.urls import path

from socialshare.views import share_email

app_name = 'socialshare'

urlpatterns = [
    path('^send-friend', share_email, name='social-share-email'),
]
