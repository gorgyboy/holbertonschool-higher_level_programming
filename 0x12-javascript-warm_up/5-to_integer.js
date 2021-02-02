#!/usr/bin/node
// Prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

const myNum = parseInt(process.argv[2]);

if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
