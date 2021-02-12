// Fetches and displays the "name" in the HTML tag DIV#character from this
// URL: https://swapi-api.hbtn.io/api/people/5/?format=json using JQuery.

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(url, function (data) {
  $('#character').text(data.name);
});
