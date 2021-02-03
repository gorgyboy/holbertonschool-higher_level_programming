#!/usr/bin/node
// Searches the second biggest integer in the list of arguments

const size = process.argv.length;
let bigger, biggest, num;
let index;

if (size <= 3) {
  console.log(0);
} else {
  biggest = parseInt(process.argv[2]);
  // We have at least to args, so we start from the second, becasue the first
  // is biggest
  for (index = 3; index < size; index++) {
    num = parseInt(process.argv[index]);
    if (num > biggest) {
      bigger = biggest;
      biggest = num;
    } else if (bigger === undefined || num > bigger) {
      bigger = num;
    }
  }
  console.log(bigger);
}
