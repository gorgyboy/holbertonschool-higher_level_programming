// Updates the text of the HTML tag HEADER to “New Header!!!” when the user
// clicks on DIV#update_header using JQuery.

$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
