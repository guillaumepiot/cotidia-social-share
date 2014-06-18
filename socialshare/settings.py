from django.conf import settings

# Whether to add a share message to the share by email form
SHARE_EMAIL_MESSAGE = getattr(settings, 'SHARE_EMAIL_MESSAGE', True)
SHARE_EMAIL_MESSAGE_PLACEHOLDER = getattr(settings, 'SHARE_EMAIL_MESSAGE_PLACEHOLDER', 'Default message goes here...')