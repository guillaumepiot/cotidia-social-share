from django import template
register = template.Library()

from socialshare.forms import ShareEmailForm
from socialshare import settings as socialshare_settings

############
# Facebook #
############

@register.inclusion_tag('socialshare/_facebook_meta.html')
def facebook_meta(title, description, image=False):
    return {'title': title, 'description':description, 'image':image }

@register.inclusion_tag('socialshare/_facebook.js')
def facebook_js():
    return {}

############
# Twitter  #
############

@register.inclusion_tag('socialshare/_twitter.js')
def twitter_js():
    return {}

############
# Tumblr   #
############

@register.inclusion_tag('socialshare/_tumblr.js')
def tumblr_js():
    return {}

##############
# LinkedIn   #
##############

@register.inclusion_tag('socialshare/_linkedin.js')
def linkedin_js():
    return {}

############
# Google   #
############

@register.inclusion_tag('socialshare/_google.js')
def google_js():
    return {}


###############
# Share email #
###############

@register.inclusion_tag('socialshare/_share_email.js')
def share_email_js():
    return {}

@register.inclusion_tag('socialshare/_share_email.html')
def share_email_html():
    initial = {
        'message':socialshare_settings.SHARE_EMAIL_MESSAGE_PLACEHOLDER
    }
    form = ShareEmailForm(initial=initial)

    if not socialshare_settings.SHARE_EMAIL_MESSAGE:
        del form.fields['message']

    return {'form':form}