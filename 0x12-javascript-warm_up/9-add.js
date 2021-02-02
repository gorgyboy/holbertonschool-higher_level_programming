#!/usr/bin/node
// Adds to arguments and prints the result

function add (a, b) {
  console.log(a + b);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
