from django import forms


class ShareEmailForm(forms.Form):
    url = forms.URLField(widget=forms.HiddenInput)
    sender_name = forms.CharField(label="You", max_length=50)
    sender_email = forms.EmailField(label="Your email address")
    friend_name = forms.CharField(label="Your friend", max_length=50)
    friend_email = forms.EmailField(label="Your friend's email address")
    message = forms.CharField(widget=forms.Textarea(), required=False)
