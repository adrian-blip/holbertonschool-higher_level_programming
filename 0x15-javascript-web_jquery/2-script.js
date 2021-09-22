$(function () {
  $("header").on( "click", "button", function( event ) {
  $(event.delegateTarget ).css( "color", "#FF0000");
});
