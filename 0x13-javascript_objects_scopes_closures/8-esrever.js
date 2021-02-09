#!/usr/bin/node

// Returns the reversed version of a list.
exports.esrever = function (list) {
  const revList = [];
  for (let revIndex = list.length - 1; revIndex >= 0; revIndex--) {
    revList.push(list[revIndex]);
  }
  return (revList);
};
