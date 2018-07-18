jQuery(document).ready(function($){





	//  Search Form

	$(".search-btnn").on("click", function(){
		$(".magazi-search-page").addClass("active")
	});
	$(".magazi-close-search").on("click", function(){
		$(".magazi-search-page").removeClass("active");
	});

	// Adding Class to links who has menu inside it

	$(".magazi-language ul li a").on("click", function(){
		$(this).parent().addClass("active").siblings().removeClass("active")
	});

	// Responsive Mobile Menu

	$(".magazi-mobil-menu .magazi-menu ul").parent().addClass("menu-item-has-children");
	$(".magazi-mobil-menu .magazi-menu li.menu-item-has-children > a").on("click", function(){
		$(this).parent().toggleClass("active").siblings().removeClass("active");
		$(this).next("ul").slideToggle();
		$(this).parent().siblings().find("ul").slideUp();
		return false;
	});


	// Sign in / Sign Up change function script

	$(".magazi-forms-heading ul li").on("click", function(){
		var tab_id = $(this).attr('data-tab');
		$(".magazi-forms-heading ul li").removeClass('current');
		$(".magazi-main-form").removeClass("current");
		$(this).addClass("current animated fadeIn");
		$("#"+tab_id).addClass("current animated fadeIn");
		return false;
	});

	$(".dls").parent().addClass("distive");

	//  Closing Filter 

	$(".close-filter").on("click", function(){
		$(this).toggleClass("active");
		$(".magazi-filter-items").slideToggle();
		return false;
	});

	//  Right Menu Open Script

	$(".menu-btn.right").on("click", function(){
		$(".magazi-right-menu.right").addClass("active");
		$("body").addClass("body-overlay");
	});
	$("html, .close-right-menu").on("click", function(){
		$(".magazi-right-menu.right").removeClass("active");
		$("body").removeClass("body-overlay");
	});
	$(".menu-btn.right, .magazi-right-menu").on("click", function(e){
		e.stopPropagation();
	});

	// Right menu open from left side

	$(".menu-btn.left").on("click", function(){
		$(".magazi-right-menu.left").addClass("active");
		$("body").addClass("body-overlay");
	});
	$("html, .close-right-menu").on("click", function(){
		$(".magazi-right-menu.left").removeClass("active");
		$("body").removeClass("body-overlay");
	});
	$(".menu-btn.left, .magazi-right-menu.left").on("click", function(e){
		e.stopPropagation();
	});

	// Cart Menu Open Script

	$(".cart-menu-btn").on("click", function(){
		$(".magazi-cart-menu").addClass("active");
		$("body").addClass("body-overlay");
	});
	$("html, .close-right-menu").on("click", function(){
		$(".magazi-cart-menu").removeClass("active");
		$("body").removeClass("body-overlay");
	});
	$(".cart-menu-btn, .magazi-cart-menu").on("click", function(e){
		e.stopPropagation();
	});

	// Wishlist Open Menu Script

	$(".wishlist-menu-btn").on("click", function(){
		$(".magazi-wishlist-menu").addClass("active");
		$("body").addClass("body-overlay");
	});
	$("html,.close-right-menu").on("click", function(){
		$(".magazi-wishlist-menu").removeClass("active");
		$("body").removeClass("body-overlay");
	});
	$(".wishlist-menu-btn, .magazi-wishlist-menu").on("click", function(e){
		e.stopPropagation();
	});


	// Responsive Menu Open

	$(".left-menu-btn").on("click", function(){
		$(".magazi-mobil-menu").addClass("active");
		$("body").addClass("body-overlay");
	});

	$("html,.close-right-menu").on("click", function(){
		$(".magazi-mobil-menu").removeClass("active");
		$("body").removeClass("body-overlay");
	});
	$(".left-menu-btn, .magazi-mobil-menu").on("click", function(e){
		e.stopPropagation();
	});

	$(".magazi-menu ul").parent().addClass("has-menu");


	//  Magazi Carousel 

	$('.magazi-carousel').slick({
		slidesToShow: 4,
		slck:true,
		slidesToScroll: 4,
		prevArrow:'<span class="slick-previous">Previous</span>',
		nextArrow:'<span class="slick-nexti">Next</span>',
		autoplay: true,
		dots: true,
		autoplaySpeed: 2000,
		responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        slidesToShow: 2,
	        slidesToScroll: 2,
	        infinite: true,
	        dots: true
	      }
	    },
	    {
	      breakpoint: 768,
	      settings: {
	        slidesToShow: 2,
	        slidesToScroll: 2
	      }
	    },
	    {
	      breakpoint: 480,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    }
	    // You can unslick at a given breakpoint now by adding:
	    // settings: "unslick"
	    // instead of a settings object
	  ]
	});
	

	// magazi-slick slrd 

	$('.magazi-slick-sldr').slick({
		slidesToShow: 1,
		slck:true,
		slidesToScroll: 1,
		prevArrow:false,
		nextArrow:false,
		autoplay: true,
		dots: false,
		centerMode:true,
		autoplaySpeed: 2000,
	});


	//  Masonary Slider

	$('.masonary-slider').slick({
		slidesToShow: 3,
		slck:true,
		centerPadding: '60px',
		slidesToScroll: 3,
		prevArrow:'<span class="slick-previous"></span>',
		nextArrow:'<span class="slick-nexti"></span>',
		autoplay: true,
		dots: true,
		centerMode:true,
		autoplaySpeed: 2000,
		responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        slidesToShow: 2,
	        slidesToScroll: 2,
	        infinite: true,
	        dots: true
	      }
	    },
	    {
	      breakpoint: 768,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    },
	    {
	      breakpoint: 480,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    }
	    // You can unslick at a given breakpoint now by adding:
	    // settings: "unslick"
	    // instead of a settings object
	  ]
	});


	// Item slider script

	 $('.slider-for').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  arrows: false,
	  fade: true,
	  dots:false,
	  asNavFor: '.slider-nav',
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1,
	        infinite: true,
	        dots: false
	      }
	    },
	    {
	      breakpoint: 768,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    },
	    {
	      breakpoint: 480,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    }
	    // You can unslick at a given breakpoint now by adding:
	    // settings: "unslick"
	    // instead of a settings object
	  ]
	});
	$('.slider-nav').slick({
	  slidesToShow: 5,
	  slidesToScroll: 1,
	  asNavFor: '.slider-for',
	  dots: false,
	  vertical: true,
	  verticalSwiping: true,
	  centerMode: false,
	  focusOnSelect: true
	});	



	//  Blog Carousel

	$('.magazi-blog-carousel').slick({
		slidesToShow: 3,
		slck:true,
		slidesToScroll: 3,
		arrows:false,
		autoplay: true,
		dots: true,
		autoplaySpeed: 2000,
		responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        slidesToShow: 2,
	        slidesToScroll: 2,
	        infinite: true,
	        dots: true
	      }
	    },
	    {
	      breakpoint: 768,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    },
	    {
	      breakpoint: 480,
	      settings: {
	        slidesToShow: 1,
	        slidesToScroll: 1
	      }
	    }
	    // You can unslick at a given breakpoint now by adding:
	    // settings: "unslick"
	    // instead of a settings object
	  ]
	});

	

	//  Blog heading Height setting

	$(".magazi-blog-heading").each(function(){

	var date_height = $(this).innerHeight();
		var date_top = date_height/3;
		$(this).find(".posting-date").css({
			"height": date_height,
			"padding-top": date_top
		});
	});

		
	// Blog info height set

	if ($(window).width() > 991) {

		var blog_height = $(".magazi-blg-img").innerHeight();
		$(".magazi-blg-info.style2").css({
			"height": blog_height
		});

	}

	// Tooltip


	$(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	});

	

	
});