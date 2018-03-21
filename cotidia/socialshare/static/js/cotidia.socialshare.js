'use strict';

(function () {
  function Facebook (elm) {
    elm.addEventListener('click', function(e) {
        e.preventDefault()
        var loc = elm.getAttribute('href')
        console.log(loc)
        window.open('https://www.facebook.com/dialog/share?app_id=' + window.facebookAppId + '&display=popup&href=' + loc)
    })
  }

  /////////////////////////////////////////////////////////////////////////////

  // Bootstrap any slideshows

  function documentReady () {
    return (document.readyState === 'interactive' || document.readyState === 'complete')
  }

  function bootstrap () {
    document.removeEventListener('readystatechange', bootstrap)

    var fb_elms = document.querySelectorAll('.share-facebook');
    Array.prototype.forEach.call(fb_elms, function (elm) {
      Facebook(elm)
    })

  }

  if (documentReady()) {
    bootstrap()
  } else {
    document.addEventListener('readystatechange', bootstrap)
  }
}())
