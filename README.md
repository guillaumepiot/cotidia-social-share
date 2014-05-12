Usage
=====

Social share generate the javascript required to share content on the following platform:

- Facebook
- Twitter
- LinkedIn
- Google+

Social share also support email sharing by generating a modal form.

* Note: Email sharing requires the Twitter Bootstrap UI and jQuery to handle the modal and form formatting *

* Note: Share functionality may not work properly if the site is run locally, as the social network won't be ablt to fetch meta data from your local page *


##Install

Add `socialshare` to your settings `INSTALLED_APPS`.

Load `socialshare_tags` in your template.
	
	{% load socialshare_tags %}


##Implementation

To call the share pop up, all you need is a link with the appropriate class and attributes.


### Facebook

	<a href="http://example.com/page-to-share" class="socialshare facebook">Share on Facebook</a>
	
The `href` attribute will be the URL that you would like to share.

Facebook requires the OpenGraph meta tags to fetch the content of the share post. So the following needs to be added on your page:

	<meta property="og:title" content="Title of the page" />
	<meta property="og:description" content="The content of the post" />
	<meta property="og:image" content="http://absolute/url/to/thumb/image" />
	
You can output those meta tags using the following template tag shortcut in the head of your page:

	{% facebook_meta 'title' 'description' 'image_url' %}
	
* `image_url` is optional *

Include the necessary javascript, as such:

	<script>
		{% facebook_js %}
	</script>
	

### Twitter

	<a href="http://example.com/page-to-share" title="The content of the tweet" class="socialshare twitter">Share on Twitter</a>
	
The `href` attribute will be the URL that you would like to share.
The `title` attribute will be the content of the tweet.

Include the necessary javascript, as such:

	<script>
		{% twitter_js %}
	</script>

### LinkedIn

	<a href="http://example.com/page-to-share" title="The title of the post" data-summary="The content of the post" class="socialshare linkedin">Share on LinkedIn</a>
	
The `href` attribute will be the URL that you would like to share.
The `title` attribute will be the title of the post.
The `data-description` attribute will be the content of the post.

Include the necessary javascript, as such:

	<script>
		{% linkedin_js %}
	</script>

### Google+

	<a href="http://example.com/page-to-share" class="socialshare google">Share on Google</a>
	
The `href` attribute will be the URL that you would like to share.

Include the necessary javascript, as such:

	<script>
		{% google_js %}
	</script>

### Share email

Add the AJAX submission url to your patterns:

	url(r'^share/', include('socialshare.urls', namespace='socialshare')),

Javascript:

The form submission requires the AJAX form Jquery plugin: http://malsup.github.io/min/jquery.form.min.js

The html:

	<a href="http://example.com/page-to-share" class="socialshare email">Share by email</a>
	
The `href` attribute will be the URL that you would like to share.

Include the tag to generate the modal form as HTML:

	{% share_email_html %}
	
Include the tag to generate the javacript for handling the form and modal:
	
	<script>
		{% share_email_js %}
	</script>
