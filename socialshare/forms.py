from django import forms
from django.utils.translation import ugettext_lazy as _

class ShareEmailForm(forms.Form):
	url = forms.URLField(widget=forms.TextInput(attrs={'style':'width:100%', 'readonly':True, 'class':"form-control"}))
	sender_name = forms.CharField(label=_('You'), max_length=50, widget=forms.TextInput(attrs={'placeholder':_('Name'), 'class':"form-control"}), error_messages={'required':_('Please enter your name')})
	sender_email = forms.CharField(label=_('Your email address'), max_length=50, widget=forms.TextInput(attrs={'placeholder':_('Email address'), 'class':"form-control"}), error_messages={'required':_('Please enter your email address')})
	friend_name = forms.CharField(label=_('Your friend'), max_length=50, widget=forms.TextInput(attrs={'placeholder':_('Name'), 'class':"form-control"}), error_messages={'required':_('Please enter your friend\'s name')})
	friend_email = forms.EmailField(label=_('Your friend\'s email address'), max_length=100, widget=forms.TextInput(attrs={'placeholder':_('Email address'), 'class':"form-control"}), error_messages={'required':_('Please enter your friend\'s email address')})
