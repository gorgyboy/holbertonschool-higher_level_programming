#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
let people = [];
let WedgeAntilles = [];

request(url, (error, response, body) => {
  if (!error) {
    for (const films of JSON.parse(body).results) {
      people = people.concat(films.characters);
    }
    WedgeAntilles = people.filter(x => x.includes('18'));
    console.log(WedgeAntilles.length);
  } else {
    console.log(error);
  }
});
