#!/usr/bin/node
// Increments number and calls a function

function addMeMaybe (number, theFunction) {
  theFunction(++number);
}

exports.addMeMaybe = addMeMaybe;
