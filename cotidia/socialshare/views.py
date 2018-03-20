import json

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from socialshare.forms import ShareEmailForm
from socialshare import settings as socialshare_settings


def share_email(request):

    errors = {}
    success = False
    initial = {}

    if request.method == "POST":
        form = ShareEmailForm(request.POST)
        if form.is_valid():
            errors = False
            success = True

            sender_name = form.cleaned_data['sender_name']
            sender_email = form.cleaned_data['sender_email']
            friend_name = form.cleaned_data['friend_name']
            friend_email = form.cleaned_data['friend_email']
            if socialshare_settings.SHARE_EMAIL_MESSAGE:
                message = form.cleaned_data['message']
            else:
                message = None
            url = form.cleaned_data['url']

            subject = 'Link referral from %s' % sender_name
            context = {
                'sender_name': sender_name,
                'sender_email': sender_email,
                'friend_name': friend_name,
                'friend_email': friend_email,
                'message': message,
                'subject': subject,
                'url': url
            }
            text_content = render_to_string('email/share_email.txt', context)
            html_content = render_to_string('email/share_email.html', context)

            msg = EmailMultiAlternatives(
                subject, text_content, '%s <%s>' % (sender_name, sender_email), [friend_email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        else:
            for field in form:
                if field.errors:
                    errors[field.name] = field.errors
    else:
        form = ShareEmailForm(initial=initial)

    results = {'error': errors, 'success': success}
    return HttpResponse(
        json.dumps(results),
        content_type='application/json'
    )
