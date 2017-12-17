$('[data-toggle="popover"]').popover({
  trigger: "manual",
}).on("mouseenter", function() {
  var _this = this;
  $(this).popover("show");
  $(".popover").on("mouseleave", function() {
    $(_this).popover('hide');
  });
}).on("mouseleave", function() {
  var _this = this;
  setTimeout(function() {
    if (!$(".popover:hover").length) {
      $(_this).popover("hide")
    }
  }, 100);
});

$("#menu-bar ul li a[href^='#']").on('click', function(e) {

  // prevent default anchor click behavior
  e.preventDefault();

  // store hash
  var hash = this.hash;

  // animate
  $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 300, function(){

      // when done, add hash to url
      // (default click behaviour)
      window.location.hash = hash;
    });
 
 });