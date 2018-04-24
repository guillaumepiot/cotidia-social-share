from cotidia.socialshare.conf import settings


def socialshare_settings(request):

    return {
        "SOCIALSHARE_FACEBOOK_APP_ID": settings.SOCIALSHARE_FACEBOOK_APP_ID,
    }
