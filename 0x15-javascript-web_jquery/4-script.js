// Toggles the class of the HTML tag HEADER when the user clicks
// on the tag DIV#toggle_header using JQuery.

$(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('green red');
  });
});
