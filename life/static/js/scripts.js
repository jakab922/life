$(window).load(function() {
	$('li.contact').click(function() {
		$('#contact_modal').fadeIn();
	});
	$('.close').click(function() {
		$('#contact_modal').fadeOut();
	});
	
	$('a.alert_box').click(function() {
		$('#alert_modal').fadeIn();
		return false;
	});
	$('.close_alerts').click(function() {
		$('#alert_modal').fadeOut();
	});
	$('#language_selector').change(function() {
		window.location.replace($('#language_selector option:selected').attr('value'));
	});
});