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

            if ($(this).scrollTop() != 0) {
                mybtn.show();
                sw=true;
            } else {
                mybtn.hide();
                sw=true;
            }

            }, 200);
        }
    });
	mybtn.click(function(){
        //$("html, body").animate({ scrollTop: 0 }, 100);
        window.scrollTo(0,0);
        return false;
    });
});