////////////////////////////
// Javascript for posts page
////////////////////////////

$(function(){
    // Executed when js-menu-icon js clicked
    $('.Js-menu-icon').click(function() {
        // $(this) : self element, namely div. Js-menu-icon
        // next() : Next to div.Js-menu-icon, namely div.menu
        // toggle() : switch show and hide 
        $(this).next().toggle();


    })

})
