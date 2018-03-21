from django import template

from cotidia.socialshare.forms import ShareEmailForm

register = template.Library()


@register.inclusion_tag('socialshare/share_email.html')
def share_email_html():
    initial = {}
    form = ShareEmailForm(initial=initial)

    return {'form': form}
