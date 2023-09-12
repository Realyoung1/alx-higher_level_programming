#!/usr/bin/node
/*
     scripted that imported a dictionary of occurrences
     Your script must import dict from the file 101-data.js
     In the new dictionary,
*/
const dict = require('./101-data').dict;

const newDict = {};
for (const obj in dict) {
  if (newDict[dict[obj]]) {
    newDict[dict[obj]] = newDict[dict[obj]].concat([obj]);
  } else {
    newDict[dict[obj]] = [obj];
  }
}
console.log(newDict);
