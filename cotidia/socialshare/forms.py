from django import forms

from betterforms.forms import BetterForm


class ShareEmailForm(BetterForm):
    url = forms.URLField(widget=forms.HiddenInput)
    sender_name = forms.CharField(label="Your name", max_length=50, widget=forms.TextInput(attrs={'autocomplete': 'name'}))
    sender_email = forms.EmailField(label="Your email address", widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
    friend_name = forms.CharField(label="Your friend's name", max_length=50, widget=forms.TextInput(attrs={'autocomplete': 'name'}))
    friend_email = forms.EmailField(label="Your friend's email address", widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

    data_title = forms.CharField(widget=forms.HiddenInput, max_length=250, required=False)
    data_excerpt = forms.CharField(widget=forms.HiddenInput, max_length=5000, required=False)
    data_image = forms.CharField(widget=forms.HiddenInput, max_length=250, required=False)
    data_action_btn = forms.CharField(widget=forms.HiddenInput, max_length=250, required=False)

    class Meta:
        fields = [
            'url',
            'sender_name',
            'sender_email',
            'friend_name',
            'friend_email',
            'message'
        ]
        fieldsets = (
            ('options', {
                'fields': (
                    ('sender_name', 'sender_email'),
                    ('friend_name', 'friend_email'),
                    'message',
                    'url',
                    'data_title',
                    'data_excerpt',
                    'data_image',
                    'data_action_btn',
                ),
                'legend': ''
            }),
        )
