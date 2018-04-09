from rest_framework import serializers


class ShareEmailSerializer(serializers.Serializer):

    url = serializers.CharField()
    sender_name = serializers.CharField()
    sender_email = serializers.EmailField()
    friend_name = serializers.CharField()
    friend_email = serializers.EmailField()
    message = serializers.CharField(required=False)

    # Share data
    data_title = serializers.CharField(required=False)
    data_excerpt = serializers.CharField(required=False)
    data_image = serializers.CharField(required=False)
    data_action_btn = serializers.CharField(required=False)

    class Meta:
        fields = (
            'url',
            'sender_name',
            'sender_email',
            'friend_name',
            'friend_email',
            'message',
            'data_title',
            'data_excerpt',
            'data_image',
            'data_action_btn'
        )
