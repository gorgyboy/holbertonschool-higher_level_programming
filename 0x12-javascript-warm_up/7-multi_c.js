#!/usr/bin/node
// Prints x times “C is fun”

let index;
const xTimes = parseInt(process.argv[2]);

if (isNaN(xTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (index = 0; index < xTimes; index++) {
    console.log('C is fun');
  }
}
