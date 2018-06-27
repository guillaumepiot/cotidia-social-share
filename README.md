Usage
=====

Social share generate the javascript required to share content on the following platform:

- Facebook
- Twitter
- LinkedIn
- Google+

Social share also support email sharing by generating a modal form.

> Note: Share functionality may not work properly if the site is run locally, as the social network won't be ablt to fetch meta data from your local page.


## Install

Add `cotidia.socialshare` `captcha` `recaptcha` to your settings `INSTALLED_APPS`.

```
INSTALLED_APPS = [
    ...
    'cotidia.socialshare',
    'captcha',
    'recaptcha',
]

```

Load `socialshare_tags` in your template.

```
{% load socialshare_tags %}
```

Include the bootstraing script on the page that needs sharing:

```html
<script type="text/javascript" src="{% static "js/cotidia.socialshare.js" %}"></script>
```

Set Facebook app id:

```python
SOCIALSHARE_FACEBOOK_APP_ID = "1234"
```

### Set up recaptcha secrets

Go to: https://www.google.com/recaptcha/intro/index.html and set up recaptcha. You should include the production and staging sites as hosts as well as localhost (but only during development)

At the end of the process you should have two secrets:
 * A public `Site` Key
 * A private `Server` Key

In settings add the following entries:

```
RECAPTCHA_PUBLIC_KEY = '<<SITE KEY>>'
RECAPTCHA_PRIVATE_KEY = '<<SERVVER KEY>>'
GR_CAPTCHA_SECRET_KEY = RECAPTCHA_PRIVATE_KEY
```
The last line is required because the rest-recaptcha and form recaptcha librarys use different variable names

### Use no captcha

Google now enforces No Captcha (mouse click in check box), use the following setting to enable it:

```python
NOCAPTCHA = True
```

## Context processor

```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
            ...
                'cotidia.socialshare.context_processor.socialshare_settings',
            ],
        },
    },
]
```

## Facebook share

Use the `share-facebook` against the link element.

E.g.:

```html
<button data-url="<full_page_url>" title="Share on Facebook" class="share-facebook">Share on Facebook</button>
```

The `data-url` attribute will be the URL that you would like to share.


## Twitter share

Use the `share-twitter` against the link element. Use `data-text` to setup a default tweet message.

E.g.:

```html
<button data-url="<full_page_url>" title="Share on Twitter" class="share-twitter" data-text="Best page ever">Share on Twitter</button>
```

The `data-url` attribute will be the URL that you would like to share.

## LinkedIn share

Use the `share-linkedin` against the link element. Use `data-title` to setup a default post title.

E.g.:

```html
<button data-url="<full_page_url>" title="Share on LinkedIn" class="share-linkedin" data-title="Best page ever">Share on LinkedIn</button>
```

The `data-url` attribute will be the URL that you would like to share.

## Google+

Use the `share-google` against the link element.

E.g.:

```html
<button data-url="<full_page_url>" title="Share on Google" class="share-google">Share on Google</button>
```

The `data-url` attribute will be the URL that you would like to share.


## Copy to clipboard

Use the `copy-clipboard` against the link element.

E.g.:

```html
<button data-url="<full_page_url>" title="Copy page url to clipboard" class="copy-clipboard">Copy to clipboard</button>
```

The `data-url` attribute will be the URL that you would like to share.


## Share email

Add the AJAX submission url to your patterns:

```python
urlpattenrs = [
    path('share/', include('cotidia.socialshare.urls', namespace='socialshare-api')),
]
```

Ensure that the socialshare Javascript is inclded on the page:

```html
<script type="text/javascript" src="{% static "js/cotidia.socialshare.js" %}"></script>
```

Output the modal form using the template tag:

```html
{% load socialshare_tags %}
{% share_email_html data_title="The title" data_excerpt="A short description" data_image="An image url" data_action_btn="Text in the email link" %}
```

Add the share link (Use the `share-email` against the link element):

```html
<button data-url="<full_page_url>" title="Email this" class="share-email">Share</button>
```

The `data-url` attribute will be the URL that you would like to share.

If you want a custom subject to the email you can add this into the settings file:
```
SOCIALSHARE_EMAIL_SUBJECT = "An email subject"
```

To include the sender's name, or invitee's name include `{sender_name}` or `{friend_name}` eg:
```
SOCIALSHARE_EMAIL_SUBJECT = "{sender_name} sent you an email"
```
