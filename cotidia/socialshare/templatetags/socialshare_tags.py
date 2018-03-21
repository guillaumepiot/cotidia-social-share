from django import template
register = template.Library()

from cotidia.socialshare.forms import ShareEmailForm

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
    initial = {}
    form = ShareEmailForm(initial=initial)

    return {'form': form}
