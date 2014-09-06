
$.noConflict();
jQuery(document).ready(function($) {

	// load masonry for membres
	if($('#blocks .block-mini').size() > 0){
		
		var $container = $('#blocks').masonry();
		
		
			
		setTimeout(function(){
			$container.imagesLoaded( function() {
				$container.masonry({
					itemSelector : '.block-mini',
					columnWidth : ($('#blocks').width() == 930) ? 310: 233,
					transitionDuration: 0
				});
			});
		},500);
		
		/*$('#blocks').masonry({
			// options
			itemSelector : '.block-mini',
			columnWidth : ($('#blocks').width() == 620) ? 310: 233,
			isAnimated : false,
			animationOptions : {
				duration : 400
			}
		});*/

		var widthBlocks = $('#blocks').width();

		$(window).resize(function(){

			if($('#blocks').width() != widthBlocks){

				widthBlocks = $('#blocks').width();
				$('#blocks').masonry( 'option', { columnWidth: ($('#blocks').width() == 930) ? 310: 233 } );
				$('#blocks').masonry( 'reload' );
			}
		});
	}
	
	
	
	// load masonry for membres
	if($('#membres .block-mini').size() > 0){
		
		var $container = $('#membres').masonry();
		setTimeout(function(){
			$container.imagesLoaded( function() {
				$container.masonry({
					itemSelector : '.block-mini',
					columnWidth : 232,
					transitionDuration: 0
				});
			});
		},200);
	}


	


	//load other
	var limit = 40;
	var limitStart = 0;
	var data = {};

	if(typeof MemberTotal != 'undefined'){
		var encour = false;
		$(window).scroll(function() {

			if ($(window).scrollTop() + $(window).height() > ($(document).height() - 200)) {

				if(encour) return;
				encour = true;

				limitStart++;
				data.limitstart = limitStart * limit;

				if( data.limitstart >= MemberTotal) return;

				data.filter_section = $('select[name="filter_section"]').val();
				data.filter_city = $('select[name="filter_city"]').val();
				data.filter_name = $('select[name="filter_name"]').val();
				data.filter_search = $('input[name="filter_search"]').val();

				$.post(window.location.pathname,data,function(response){

					var $content = $(response.replace(/^\s+/g,'').replace(/\s+$/g,''));
					$container.append( $content );
					$container.imagesLoaded( function() {
						$container.masonry( 'appended', $content, true );
					});
					encour = false;
				});
			}
		});
	}


});