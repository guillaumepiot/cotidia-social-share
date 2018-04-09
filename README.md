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

Add `cotidia.socialshare` to your settings `INSTALLED_APPS`.

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
<a href="<full_page_url>" title="Share on Facebook" class="share-facebook">Share on Facebook</a>
```

The `href` attribute will be the URL that you would like to share.


## Twitter share

Use the `share-twitter` against the link element. Use `data-text` to setup a default tweet message.

E.g.:

```html
<a href="<full_page_url>" title="Share on Twitter" class="share-twitter" data-text="Best page ever">Share on Twitter</a>
```

The `href` attribute will be the URL that you would like to share.

## LinkedIn share

Use the `share-linkedin` against the link element. Use `data-title` to setup a default post title.

E.g.:

```html
<a href="<full_page_url>" title="Share on LinkedIn" class="share-linkedin" data-title="Best page ever">Share on LinkedIn</a>
```

The `href` attribute will be the URL that you would like to share.

## Google+

Use the `share-google` against the link element.

E.g.:

```html
<a href="<full_page_url>" title="Share on Google" class="share-google">Share on Google</a>
```

The `href` attribute will be the URL that you would like to share.

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

The `href` attribute will be the URL that you would like to share.
