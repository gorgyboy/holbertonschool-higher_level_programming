// Adds the class red to the HTML tag HEADER when the user clicks on the
// tag DIV#red_header using JQuery.

$(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
