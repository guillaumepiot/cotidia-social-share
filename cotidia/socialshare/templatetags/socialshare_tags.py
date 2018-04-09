from django import template

from cotidia.socialshare.forms import ShareEmailForm

register = template.Library()


@register.inclusion_tag('socialshare/share_email.html')
def share_email_html(
        data_title=None,
        data_excerpt=None,
        data_image=None,
        data_action_btn=None):
    initial = {}
    if data_title:
        initial['data_title'] = data_title
    if data_excerpt:
        initial['data_excerpt'] = data_excerpt
    if data_image:
        initial['data_image'] = data_image
    if data_action_btn:
        initial['data_action_btn'] = data_action_btn

    print('initial', initial)

    form = ShareEmailForm(initial=initial)

    return {'form': form}
