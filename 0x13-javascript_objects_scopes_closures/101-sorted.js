#!/usr/bin/node
// Imports a dictionary of occurrences by user id and computes a dictionary
// of user ids by occurrence.

const dict = require('./101-data.js').dict;
let newDict = new Object();

for (const key in dict) {
  if (!(newDict.hasOwnProperty(key))) {
    newDict[dict[key]] = [];
  }
}

for (const key in dict) {
  newDict[dict[key]].push(key);
}

console.log(newDict);
