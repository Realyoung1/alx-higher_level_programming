#!/usr/bin/node
/*
  this script computed and printed factorials
*/

function factorial (q) {
  if (q === 1 || isNaN(q)) {
    return 1;
  }
  return q * factorial(q - 1);
}

const args = process.argv;

console.log(factorial(parseInt(args[2])));
