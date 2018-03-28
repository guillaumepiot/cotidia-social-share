from django.conf import settings

from appconf import AppConf


class SocialShareConf(AppConf):

    FACEBOOK_APP_ID = "[Not implemented]"

    class Meta:
        prefix = 'socialshare'
