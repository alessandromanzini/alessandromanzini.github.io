$(document).ready(function(){
    let flag = false;
    $(this).keypress(function(){if(event.which == 110)
        if(flag=!flag){ $("nav").addClass("navbar-light bg-light"); $("nav").removeClass("navbar-dark bg-dark")}
        else{ $("nav").removeClass("navbar-light bg-light"); $("nav").addClass("navbar-dark bg-dark")}
    })
})