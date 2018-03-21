from django.conf import settings

from cotidia.mail.notice import Notice


class ShareEmailNotice(Notice):
    # Use as a list display
    name = 'Share email'
    # Use for the preview URL as a slug, so it must not contains
    # spaces or other symbols than lowercase letters and hyphens
    identifier = 'share-email'
    # Defines an HTML template for this notice
    html_template = 'email/share_email.html'
    text_template = 'email/share_email.txt'

    # A context passed to every request (merge with `context`)
    default_context = {
        'SITE_URL': settings.SITE_URL
    }

    # A JSON representation of the context dictionary,
    # which is the format it will be saved as in the EmailLog
    context = {
        "sender_name": "Guillaume",
        "friend_name": "Frank",
        "message": "I think you will like this, check it out.",
        "url": "/admin/crm/enquiry/21/"
    }

    # Passing on come context variables to build the subject line
    subject = 'Guillaume has shared a page with you'
