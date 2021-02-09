#!/usr/bin/node

// Returns the number of occurrences of searchElement in a list.
exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  for (const element of list) {
    if (element === searchElement) {
      nb++;
    }
  }
  return (nb);
};
