#!/usr/bin/node
/*
    this is the fun which returned number of occurrences in a list:
    Prototype: exports.nbOccurences = function (list, searchElement)
*/
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count += 1;
    }
  }
  return count;
};
