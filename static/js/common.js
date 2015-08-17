/* SUMSCOPE Common Javascript
 * Created: 2015-02-13
 * Update: ----
 * Author: JollyJ
 * Copyright: SUMSCOPE
 */

//首页背景图片定位,导航栏自适应高度等
$(function() {


	$("input[type=text]").focus(function(){
		$(this).addClass("focus");
	});
	$("input[type=text]").blur(function(){
		$(this).removeClass("focus");
	});
	$("input[type=text]").hover(
		function(){
			if($(this).is(":focus")==false){$(this).addClass("hover");}
		},
		function(){
			if($(this).is(":focus")==false){$(this).removeClass("hover");}
		}
	);
	$("input.btn").hover(
		function(){
			$(this).addClass("hover");
		},
		function(){
			$(this).removeClass("hover");
		}
	);

	//Resize Canvas
	function resizeCanvas()
	{
		var pw = $(window).width();
		var ph = $(window).height();
		var sw = $("#sideBar").width();

		$("#content").css("width",pw);
		$("#headerTitle").css({"width":pw-sw});
		$("#content").css("height",ph);
		$("#sideBar").css("height",ph);
	}
	resizeCanvas();
	$(window).resize(function(){resizeCanvas();});

	//Scroll Switch
	$(window).scroll(function(){
		if($(window).scrollTop() > 50)
			{
				$("header").addClass("fixed");
				$("#headerTitle").addClass("fixed");
			}
		else{
				$("header").removeClass();
				$("#headerTitle").removeClass();
		}
	});

})


