'use strict';

(function () {

  var shareEmailModal = document.querySelector('.share-email-modal')
  if (shareEmailModal) {
    let shareEmailModalCloseBtns = document.querySelectorAll('.close-dialog')
    if (shareEmailModalCloseBtns) {
      Array.prototype.forEach.call(shareEmailModalCloseBtns, function (elm) {
        elm.addEventListener('click', function() {
          shareEmailModal.classList.remove('dialog--modal-open')
        })
      })
    }
  }

  function getPopupArgs () {
    let args = 'height=450, width=550, top=0, left=0, toolbar=0, location=0, menubar=0, directories=0, scrollbars=0'
    console.log(args)
    return args
  }

  function Facebook (elm) {
    elm.addEventListener('click', function(e) {
        e.preventDefault()
        let loc = elm.dataset.url
        if (!loc) loc = elm.getAttribute('href')
        window.open('https://www.facebook.com/dialog/share?app_id=' + window.facebookAppId + '&display=popup&href=' + loc, 'facebookwindow', getPopupArgs())
    })
  }

  function Google (elm) {
    elm.addEventListener('click', function(e) {
        e.preventDefault()
        let loc = elm.dataset.url
        if (!loc) loc = elm.getAttribute('href')
        window.open('https://plus.google.com/share?url=' + loc, 'googlewindow', getPopupArgs())
    })
  }

  function LinkedIn (elm) {
    elm.addEventListener('click', function(e) {
        e.preventDefault()
        let loc = elm.dataset.url
        if (!loc) loc = elm.getAttribute('href')
        let title = elm.dataset.title
        window.open('http://www.linkedin.com/shareArticle?mini=true&url=' + loc + '&title=' + title, 'linkedinwindow', getPopupArgs())
    })
  }

  function Twitter (elm) {
    elm.addEventListener('click', function(e) {
        e.preventDefault()
        let loc = elm.dataset.url
        if (!loc) loc = elm.getAttribute('href')
        let text = elm.dataset.text
        window.open('http://twitter.com/share?url=' + loc + '&text=' + text, 'twitterwindow', getPopupArgs())
    })
  }

  function Email (elm) {
    elm.addEventListener('click', function(e) {
        e.preventDefault()
        let loc = 'url' in elm.dataset ? elm.dataset.url : null
        shareEmailModal.classList.add('dialog--modal-open')
        let urlInput = document.querySelector('input#id_url')
        if (loc) urlInput.value = loc
        let successMessage = document.querySelector('form.share-email-form .success-message');
        if (successMessage) successMessage.remove()
    })
  }

  // Copy to clipboard

  function fallbackCopyTextToClipboard (elm) {
    var textArea = document.createElement("textarea");
    textArea.value = elm.dataset.url;
    elm.parentNode.insertBefore(textArea, elm.nextSibling);
    textArea.focus();
    textArea.select();

    try {
      var successful = document.execCommand('copy');
      var msg = successful ? 'successful' : 'unsuccessful';
    } catch (err) {
      console.error('Fallback: Oops, unable to copy', err);
    }

    textArea.remove()
  }

  function copyTextToClipboard (elm) {
    if (!navigator.clipboard) {
      fallbackCopyTextToClipboard(elm);
      return;
    }
    navigator.clipboard.writeText(elm.dataset.url).then(function() {
    }, function(err) {
      console.error('Async: Could not copy text: ', err);
    });
  }

  // Share email

  function send (elm, data) {
    setLoading(elm)

    var xhr = new XMLHttpRequest()

    xhr.onerror = function (e) {
      console.error('Error sending.')
    }

    xhr.onload = function () {
      unsetLoading(elm)

      if(xhr.status === 400) {
        var errorData = JSON.parse(xhr.responseText)
        clearFormError(elm)
        for (var key in errorData) {
          if (errorData.hasOwnProperty(key)) {
              displayFieldError(elm, key, errorData[key])
          }
        }
      }

      if(xhr.status >= 200 && xhr.status < 300) {
        elm.reset()
        clearFormError(elm)
        // Try remove the alert if there
        let alertElm = elm.querySelector('.alert')
        if (alertElm) {
          alertElm.remove()
        }
        var successData = JSON.parse(xhr.responseText)
        var successNode = document.createElement("div")
        successNode.className = 'alert alert--success'
        successNode.innerHTML = successData['message']
        var successNodeWrapper = document.createElement("div")
        successNodeWrapper.className = 'form__row success-message'
        successNodeWrapper.style.display = "block"
        successNodeWrapper.prepend(successNode)
        elm.querySelector('.dialog__body fieldset').prepend(successNodeWrapper)
        var event = new Event('formfieldsetclass');
        document.dispatchEvent(event);
      }

    };

    xhr.open('POST', elm.dataset.url)
    xhr.send(data)
  }

  function clearFormError (elm) {
    elm.querySelectorAll('.form__group--error').forEach(function (group) {
      group.classList.remove('form__group--error')
      var errorNode = group.querySelector(".form__help")
      // Save original help text
      errorNode.innerHTML = errorNode.dataset.help
    })
  }

  function displayFieldError (elm, field, error_message){
    var formField = elm.querySelector('[name=' + field + ']')
    // Add error class
    while (!formField.classList.contains('form__group')) {
      formField = formField.parentNode
    }
    formField.classList.add('form__group--error')
    // Display error
    var errorNode = formField.querySelector(".form__help")
    // Save original help text
    errorNode.dataset.help = errorNode.innerHTML
    errorNode.innerHTML = error_message[0]
    formField.appendChild(errorNode)
  }

  function setLoading (elm) {
    elm.querySelector('[type=submit]').classList.add('btn--loading')
  }

  function unsetLoading (elm) {
    elm.querySelector('[type=submit]').classList.remove('btn--loading')
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

    var gl_elms = document.querySelectorAll('.share-google');
    Array.prototype.forEach.call(gl_elms, function (elm) {
      Google(elm)
    })

    var lk_elms = document.querySelectorAll('.share-linkedin');
    Array.prototype.forEach.call(lk_elms, function (elm) {
      LinkedIn(elm)
    })

    var tw_elms = document.querySelectorAll('.share-twitter');
    Array.prototype.forEach.call(tw_elms, function (elm) {
      Twitter(elm)
    })

    var email_elms = document.querySelectorAll('.share-email');
    Array.prototype.forEach.call(email_elms, function (elm) {
      Email(elm)
    })

    var copy_elms = document.querySelectorAll('.copy-clipboard');
    Array.prototype.forEach.call(copy_elms, function (elm) {
      elm.addEventListener('click', function(event) {
        event.preventDefault()
        copyTextToClipboard(elm);
      });
    })



    document.querySelectorAll("form.share-email-form").forEach(function (elm) {
      elm.addEventListener("submit", function (e) {
        e.preventDefault()
        var formData = new FormData(elm)
        send(elm, formData)
      })
    })
  }

  if (documentReady()) {
    bootstrap()
  } else {
    document.addEventListener('readystatechange', bootstrap)
  }
}())
