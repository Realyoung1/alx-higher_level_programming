#!/usr/bin/node
/*
  this code printed the additions of two integers q,w
*/

function add (q, w) {
  return parseInt(q) + parseInt(w);
}

const args = process.argv;

console.log(add(args[2], args[3]));
