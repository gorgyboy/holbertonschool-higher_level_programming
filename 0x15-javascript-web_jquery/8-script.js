// Fetches and lists the "title" for all movies in the HTML tag UL#list_movies
// from this URL: https://swapi-api.hbtn.io/api/films/?format=json using
// JQuery.

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(url, function (data) {
  for (const movie of data.results) {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  }
});
