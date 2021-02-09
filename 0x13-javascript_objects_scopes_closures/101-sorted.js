#!/usr/bin/node
// Imports a dictionary of occurrences by user id and computes a dictionary
// of user ids by occurrence.

const dict = require('./101-data.js').dict;
const newDict = {};

for (const key in dict) {
  if (!(key in newDict)) {
    newDict[dict[key]] = [];
  }
}

for (const key in dict) {
  newDict[dict[key]].push(key);
}

console.log(newDict);
