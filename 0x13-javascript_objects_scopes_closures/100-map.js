#!/usr/bin/node
// Imports an array and computes a new array.

const list = require('./100-data.js').list;

const mappedList = list.map(function (element, index) {
  return (element * index);
});

console.log(list);
console.log(mappedList);
