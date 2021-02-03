#!/usr/bin/node
// Searches the second biggest integer in the list of arguments

const size = process.argv.length;
let bigger, biggest;
let index;

if (size <= 3) {
  console.log(0);
} else {
  bigger = parseInt(process.argv[2]);
  biggest = parseInt(process.argv[2]);
  // We have at least to args, so we start from the second, becasue the first
  // is bigger and biggest
  for (index = 3; index < size; index++) {
    if (process.argv[index] > biggest) {
      bigger = biggest;
      biggest = parseInt(process.argv[index]);
    }
  }
  console.log(bigger);
}
