from django.db import transaction

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from cotidia.socialshare.serializers import ShareEmailSerializer
from cotidia.socialshare.notices import ShareEmailNotice


class ShareEmail(APIView):
    """A public api views to share by email."""

    authentication_classes = ()
    permission_classes = ()

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        success_message = kwargs.get(
            "success_message",
            "The page has been shared."
        )

        serializer = ShareEmailSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data

            url = data.get('url')
            sender_name = data.get('sender_name')
            sender_email = data.get('sender_email')
            friend_name = data.get('friend_name')
            friend_email = data.get('friend_email')
            message = data.get('message')
            data_title = data.get('data_title')
            data_excerpt = data.get('data_excerpt')
            data_image = data.get('data_image')
            data_action_btn = data.get('data_action_btn')

            sender = '{} <{}>'.format(sender_name, sender_email)
            recipients = ['{} <{}>'.format(friend_name, friend_email)]
            reply_to = sender
            subject = "{} has shared a page with you".format(sender_name)

            context = {
                'url': url,
                'sender_name': sender_name,
                'friend_name': friend_name,
                'message': message,
                'data_title': data_title,
                'data_excerpt': data_excerpt,
                'data_image': data_image,
                'data_action_btn': data_action_btn
            }

            print(context)

            notice = ShareEmailNotice(
                subject=subject,
                sender=sender,
                reply_to=reply_to,
                recipients=recipients,
                context=context
            )

            # Send the notice straight away
            notice.send()

            data = {
                "message": success_message,
                "data": serializer.data
            }

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
