$(document).ready(function(){
    $(this).scroll(function(){
        if($(window).scrollTop()>20) $("nav").addClass("navbar-dark bg-dark")
        else $("nav").removeClass("navbar-dark bg-dark")
    })

    $("nav").hover(
        function(){
            $(this).find("li").animate({marginLeft:'15px'},'fast')
        },
        function() {
            $(this).find("li").animate({marginLeft:'0px'},'fast')
        }
    )
})