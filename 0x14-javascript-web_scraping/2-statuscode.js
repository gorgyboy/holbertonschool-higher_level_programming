#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = process.argv[2];
request(url, (error, response) => {
  console.log(error || `code: ${response.statusCode}`);
});
