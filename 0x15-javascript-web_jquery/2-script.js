// Updates the text color of the HTML tag HEADER to red (#FF0000) when the user
// clicks on the tag DIV#red_header using JQuery.

$(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
