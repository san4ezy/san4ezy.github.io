$(document).ready(function(){

	//slider
	$('.portfolio-slider').slick({
	  infinite: true,
	  arrows: true,
	  dots: false,
	  nextArrow: '<button class="slick-arrow slick-next"></button>',
 	  prevArrow: '<button class="slick-arrow slick-prev"></button>',
	  slidesToShow: 3,
	  slidesToScroll: 1,
	  autoplay:true,
	  autoplaySpeed:10000,
	  speed:1000,
	  responsive: [
	    {
	      breakpoint: 950,
	      settings: {
		      slidesToShow: 2
			  }
	    },
	    {
	      breakpoint: 600,
	      settings: {
		      slidesToShow: 1
			  }
	    }
	  ]
	});

	//modal
	var modalCont = $('.modal'),
		modalOver = $('.modal-overlay');
		
	$('.button-modal').on('click',function(e){
		e.preventDefault();
		var id = $(this).attr('href');
		$(id).addClass('modal-open');
		$(modalOver).addClass('open-overlay');
	});

	$('.cancel').on('click',function(){
		$(modalCont).removeClass('modal-open');
		$(modalOver).removeClass('open-overlay');
	});
	$(modalOver).on('click',function(){
		$(modalCont).removeClass('modal-open');
		$(modalOver).removeClass('open-overlay');
	});

	// menu
	var head = $('.header'),
		headList = $('.header-item');

	$(headList).on('click', 'a', function(e){
		e.preventDefault();
		var itemId = $(this).attr('href'),
				blockTop = $(itemId).offset().top;
		$('html, body').animate({scrollTop : blockTop - $(head).height()},900);

		$(head).removeClass('header-open');
		$('.header-nav').slideToggle(100);

	});

	// scroll menu
	$(window).scroll(function(){
		if($(this).scrollTop() > 20)
			$('.header').addClass('fixed');
		else
			$('.header').removeClass('fixed');
	});

	// mob menu
	$('.menu-bar').on('click', function(){
		$('.header').toggleClass('header-open');
		$('.header-nav').slideToggle(100);
	});

});