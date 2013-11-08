$(document).on('click', '.socialshare.tumblr', function(e){
 
  //We tell our browser not to follow that link
  e.preventDefault();
 
  //We get the URL of the link
  var loc = escape($(this).attr('href'));
  var title = escape($(this).attr('title'));
  var description = escape($(this).attr('data-description'));
  //We trigger a new window with the Twitter dialog, in the middle of the page
  window.open('http://www.tumblr.com/share/link?url=' + loc + '&name=' + title + '&description=' + description +'&', 'facebookwindow', 'height=450, width=550, top='+($(window).height()/2 - 225) +', left='+$(window).width()/2 +', toolbar=0, location=0, menubar=0, directories=0, scrollbars=0');
 
});