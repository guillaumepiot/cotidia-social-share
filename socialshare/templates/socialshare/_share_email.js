{% load i18n %}
$('.socialshare.email').click(function(e){
	e.preventDefault();
 	$('#share-email-modal').modal();
 	$('#share-email-modal').find('#id_url').val($(this).attr('href'));
});

var options = { 
beforeSubmit: function(){
	$('.submit').attr('value','{% trans "Sending..." %}');
},
success: function(data) { 

		$('.alert').remove();
		if(data.error){
			$('.submit').attr('value','{% trans "Send" %}');
			// Clear error class first
			$('input').removeClass('error');
			$.each(data.error, function(index, value) { 
				$('[name="'+index+'"]').addClass('error');
			})

			$('#form-share-email').prepend('<div class="alert alert-error"></div>');
			$.each(data.error, function(index, value) { 
				$('#form-share-email .alert').append(value+'<br>');
			})
		}
		if(data.success){
			$('input[type=text]').removeClass('error')
			$('input[name=sender_name]').attr('value','');
			$('input[name=sender_email]').attr('value','');
			$('input[name=friend_name]').attr('value','');
			$('input[name=friend_email]').attr('value','');
			$('.submit').attr('value','{% trans "Send" %}');
			$('#form-share-email').before('<div class="alert alert-success">{% trans "The event link has been sent to your friend" %}</div>');
			setTimeout("$('#share-email-modal').modal('hide');", 2000);
		}
        
    } 
}; 

$('#form-share-email').ajaxForm(options);