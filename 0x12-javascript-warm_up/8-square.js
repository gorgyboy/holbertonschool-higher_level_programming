#!/usr/bin/node
// Prints a square

let indexV, indexH;
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Store in squareRow 'size' times 'X' to create the square's row
  let squareRow = '';
  for (indexH = 0; indexH < size; indexH++) {
    squareRow += 'X'
  }
  // Print squareRow 'size' times
  for (indexV = 0; indexV < size; indexV++) {
    console.log(squareRow);
  }
}
