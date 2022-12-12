$(document).ready(function(){
    var mybtn = $('#myBtn')

	mybtn.click(function(){
		$('body, html').animate({
			scrollTop: 0
		}, 500);
	});

	$(window).scroll(function(){
		if( $(this).scrollTop() > 100 ){
			mybtn.slideDown(500);
		} else {
			mybtn.slideUp(500);
		}
	});
});