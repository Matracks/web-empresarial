$(document).ready(function(){
    var mybtn = $('#myBtn')

	// mybtn.click(function(){
	// 	$('body, html').animate({
	// 		scrollTop: 0
	// 	}, 500);
	// });

	// $(window).scroll(function(){
	// 	if( $(this).scrollTop() > 100 ){
	// 		mybtn.slideDown(500);
	// 	} else {
	// 		mybtn.slideUp(500);
	// 	}
	// });

	var sw=true;
    $(window).scroll(function () {
        if(sw){
            sw=false;
            setTimeout(function(){

            if ($(this).scrollTop() > 100) {
                mybtn.slideDown(400);
                sw=true;
            } else {
                mybtn.slideUp(400);
                sw=true;
            }

            }, 200);
        }
    });
	
	mybtn.click(function(){
		$('body, html').animate({
			scrollTop: 0
		}, 500);
		});
    // window.scrollTo(0,0);
    return false;
    
});