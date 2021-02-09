#!/usr/bin/node
// Prints the number of arguments already printed and the new argument value.

exports.logMe = (function () {
  let counter = 0;
  return function (item) {
    console.log(`${counter}: ${item}`);
    counter++;
  }
})();
