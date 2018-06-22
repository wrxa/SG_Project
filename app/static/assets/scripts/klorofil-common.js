$(document).ready(function() {

	$('#breadcrumbSwitch').on('click', function() {
		// 点击隐藏
		if($('.breadcrumb-fix').hasClass('show')) {
			$('.breadcrumb-fix').removeClass('show');
			$('.breadcrumb-fix').addClass('hide');
			$('.eye').removeClass('hide');
			$('.eye-hide').addClass('hide');
			// $('#breadcrumbSwitch').attr("data-flag", "0");
			$('.full-width-style').addClass("top-bread");
			$('.full-width-style').removeAttr("style");
		// 点击出现
		}else{
			$('.breadcrumb-fix').removeClass('hide');
			$('.breadcrumb-fix').addClass('show');
			$('.eye-hide').removeClass('hide');
			$('.eye').addClass('hide');
			// $('#breadcrumbSwitch').attr("data-flag", "1");
			$('.full-width-style').removeClass("top-bread");
			if($('body').hasClass('layout-fullwidth')) {
			$('.full-width-style').css("margin-top", "15px");
		}
	}
	});
	
		/*-----------------------------------/
		/*	TOP NAVIGATION AND LAYOUT
		/*----------------------------------*/
	
		$('.btn-toggle-fullwidth').on('click', function() {
			// 小，点击放大
			if(!$('body').hasClass('layout-fullwidth')) {
				$('.main-content').removeClass('width88');
				$('.breadcrumb-fix').removeClass('width88');
				// if($("#menuSelect").val() == "ccppplanList"){
					$('.breadcrumb-fix').css("height", '55px');
					// alert("ee");
				// }
				if($('.breadcrumb-fix').hasClass('show')) {
						$('.full-width-style').css("margin-top", "5px");
				}
				$('.full-width-style').removeClass('width-little');
				$('body').addClass('layout-fullwidth');
			// 大，点击缩小
			} else {
				$('body').removeClass('layout-fullwidth');
				$('.main-content').addClass('width88');
				$('.breadcrumb-fix').addClass('width88');
				// $('.breadcrumb-fix').css("height", '96px');
				// $('.full-width-style').addClass('width-little');
				$('.full-width-style').removeAttr("style");
				$('body').removeClass('layout-default'); // also remove default behaviour if set
			}
	
			$(this).find('.lnr').toggleClass('lnr-arrow-left-circle lnr-arrow-right-circle');
	
			if($(window).innerWidth() < 1025) {
				if(!$('body').hasClass('offcanvas-active')) {
					$('body').addClass('offcanvas-active');
				} else {
					$('body').removeClass('offcanvas-active');
				}
			}
		});
	
		$(window).on('load', function() {
			if($(window).innerWidth() < 1025) {
				$('.btn-toggle-fullwidth').find('.icon-arrows')
				.removeClass('icon-arrows-move-left')
				.addClass('icon-arrows-move-right');
			}
	
			// adjust right sidebar top position
			$('.right-sidebar').css('top', $('.navbar').innerHeight());
	
			// if page has content-menu, set top padding of main-content
			if($('.has-content-menu').length > 0) {
				$('.navbar + .main-content').css('padding-top', $('.navbar').innerHeight());
			}
	
			// for shorter main content
			if($('.main').height() < $('#sidebar-nav').height()) {
				$('.main').css('min-height', $('#sidebar-nav').height());
			}
		});
	
	
		/*-----------------------------------/
		/*	SIDEBAR NAVIGATION
		/*----------------------------------*/
	
		$('.sidebar a[data-toggle="collapse"]').on('click', function() {
			var leftMeun = ['collapsed index', 'coalCHPplanList', 'coalCHPreport', 'coalCHPequipmentList',
			'biomassplanList', 'biomassreport', 'biomassEquipmentTemplate',
			'biomassreporttemplateList', 'biomassFuelMaintain', 'ccppreporttemplateList',
			'gpgreporttemplateList', 'coalCHPreporttemplateList',
			'ccppplanList', 'ccppreport', 'ccppequipmenttemplateList', 
			'gpgplanList', 'gpgreport', 'energyisland_questionnaire', 'energyisland_addDevice', 'energyisland_graph',
			'energyIslandplanList'
			];
			// , 'energyIslandreport', 'energyIslandtemplateList'
			// 不走后台时菜单清除除下拉菜单以外的选中状态
			var thisClass = "";
			if($(this).hasClass('collapsed')) {
				thisClass = $(this).attr("class");
			}
			for (var i = 0; i < leftMeun.length; i++) {
				if(thisClass != leftMeun[i]) {
					$("." + leftMeun[i]).removeClass('active');
				}
			}
			if($(this).hasClass('collapsed')) {
				$(this).addClass('active');
			} else {
				$(this).removeClass('active');
			}
		});
	
		// if( $('.sidebar-scroll').length > 0 ) {
		// 	$('.sidebar-scroll').slimScroll({
		// 		height: '95%',
		// 		wheelStep: 2,
		// 	});
		// }
	
	
		/*-----------------------------------/
		/*	PANEL FUNCTIONS
		/*----------------------------------*/
	
		// panel remove
		$('.panel .btn-remove').click(function(e){
	
			e.preventDefault();
			$(this).parents('.panel').fadeOut(300, function(){
				$(this).remove();
			});
		});
	
		// panel collapse/expand
		var affectedElement = $('.panel-body');
	
		// $('.panel .btn-toggle-collapse').clickToggle(
		// 	function(e) {
		// 		e.preventDefault();
	
		// 		// if has scroll
		// 		if( $(this).parents('.panel').find('.slimScrollDiv').length > 0 ) {
		// 			affectedElement = $('.slimScrollDiv');
		// 		}
	
		// 		$(this).parents('.panel').find(affectedElement).slideUp(300);
		// 		$(this).find('i.lnr-chevron-up').toggleClass('lnr-chevron-down');
		// 	},
		// 	function(e) {
		// 		e.preventDefault();
	
		// 		// if has scroll
		// 		if( $(this).parents('.panel').find('.slimScrollDiv').length > 0 ) {
		// 			affectedElement = $('.slimScrollDiv');
		// 		}
	
		// 		$(this).parents('.panel').find(affectedElement).slideDown(300);
		// 		$(this).find('i.lnr-chevron-up').toggleClass('lnr-chevron-down');
		// 	}
		// );
	
	
		/*-----------------------------------/
		/*	PANEL SCROLLING
		/*----------------------------------*/
	
		// if( $('.panel-scrolling').length > 0) {
		// 	$('.panel-scrolling .panel-body').slimScroll({
		// 		height: '430px',
		// 		wheelStep: 2,
		// 	});
		// }
	
		if( $('#panel-scrolling-demo').length > 0) {
			$('#panel-scrolling-demo .panel-body').slimScroll({
				height: '175px',
				wheelStep: 2,
			});
		}
	
		/*-----------------------------------/
		/*	TODO LIST
		/*----------------------------------*/
	
		$('.todo-list input').change( function() {
			if( $(this).prop('checked') ) {
				$(this).parents('li').addClass('completed');
			}else {
				$(this).parents('li').removeClass('completed');
			}
		});
	
	
		/*-----------------------------------/
		/* TOASTR NOTIFICATION
		/*----------------------------------*/
	
		if($('#toastr-demo').length > 0) {
			toastr.options.timeOut = "false";
			toastr.options.closeButton = true;
			toastr['info']('Hi there, this is notification demo with HTML support. So, you can add HTML elements like <a href="#">this link</a>');
	
			$('.btn-toastr').on('click', function() {
				$context = $(this).data('context');
				$message = $(this).data('message');
				$position = $(this).data('position');
	
				if($context == '') {
					$context = 'info';
				}
	
				if($position == '') {
					$positionClass = 'toast-left-top';
				} else {
					$positionClass = 'toast-' + $position;
				}
	
				toastr.remove();
				toastr[$context]($message, '' , { positionClass: $positionClass });
			});
	
			$('#toastr-callback1').on('click', function() {
				$message = $(this).data('message');
	
				toastr.options = {
					"timeOut": "300",
					"onShown": function() { alert('onShown callback'); },
					"onHidden": function() { alert('onHidden callback'); }
				}
	
				toastr['info']($message);
			});
	
			$('#toastr-callback2').on('click', function() {
				$message = $(this).data('message');
	
				toastr.options = {
					"timeOut": "10000",
					"onclick": function() { alert('onclick callback'); },
				}
	
				toastr['info']($message);
	
			});
	
			$('#toastr-callback3').on('click', function() {
				$message = $(this).data('message');
	
				toastr.options = {
					"timeOut": "10000",
					"closeButton": true,
					"onCloseClick": function() { alert('onCloseClick callback'); }
				}
	
				toastr['info']($message);
			});
		}
	});
	
	// toggle function
	$.fn.clickToggle = function( f1, f2 ) {
		return this.each( function() {
			var clicked = false;
			$(this).bind('click', function() {
				if(clicked) {
					clicked = false;
					return f2.apply(this, arguments);
				}
	
				clicked = true;
				return f1.apply(this, arguments);
			});
		});
	
	}
	
	
	
