from rest_framework import serializers
from recaptcha.fields import ReCaptchaField


class ShareEmailSerializer(serializers.Serializer):

    url = serializers.CharField()
    sender_name = serializers.CharField()
    sender_email = serializers.EmailField()
    friend_name = serializers.CharField()
    friend_email = serializers.EmailField()
    message = serializers.CharField(required=False)
    captcha = ReCaptchaField(write_only=True, required=False)

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
            'captcha',
            'data_title',
            'data_excerpt',
            'data_image',
            'data_action_btn'
        )

    def __init__(self, *args, **kwargs):
        data = kwargs.get("data", False)
        if data:
            initial_data = data.copy()
            initial_data["captcha"] = data.get("g-recaptcha-response","Invalid")
            kwargs["data"] = initial_data
        super().__init__(*args, **kwargs)