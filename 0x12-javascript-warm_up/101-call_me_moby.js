#!/usr/bin/node
// Executes x times a function

function callMeMoby (x, theFunction) {
  let index;
  for (index = 0; index < x; index++) {
    theFunction();
  }
}

exports.callMeMoby = callMeMoby;
