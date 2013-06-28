// We bind a new event to our link
$('.socialshare.linkedin').click(function(e){
 
  //We tell our browser not to follow that link
  e.preventDefault();
 
  //We get the URL of the link
  var loc = escape($(this).attr('href'));
 
  //We get the title of the link
  var title  = escape($(this).attr('title'));
  var summary = escape($(this).attr('data-summary'));
 
  //We trigger a new window with the Twitter dialog, in the middle of the page
  window.open('http://www.linkedin.com/shareArticle?mini=true&url=' + loc + '&title=' + title +'&summary=' + summary, 'twitterwindow', 'height=450, width=550, top='+($(window).height()/2 - 225) +', left='+$(window).width()/2 +', toolbar=0, location=0, menubar=0, directories=0, scrollbars=0');
 
});