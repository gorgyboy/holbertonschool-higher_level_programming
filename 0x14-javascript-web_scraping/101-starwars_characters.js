#!/usr/bin/node

// Prints all characters of a Star Wars movie. Displays one character name by
// line in the same order of the list “characters” in the /films/ response.

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
const orderedChars = {};
request(url, (error, response, content) => {
  if (!error) {
    const people = JSON.parse(content).characters;
    people.forEach((character) => {
      request(character, (error, response, content) => {
        if (!error) {
          orderedChars[character.split('/')[5]] = JSON.parse(content).name;
          if (Object.entries(orderedChars).length === people.length) {
            Object.values(orderedChars).forEach((element) => {
              console.log(element);
            });
          }
        }
      });
    });
  }
});
