#!/usr/bin/node
/*
     func that imported the array and computed new array
     Your script must import list from the file 100-data.js
     Print both the initial list and the new list
*/

const list = require('./100-data').list;
const newList = list.map((element, index) => element * index);
console.log(list);
console.log(newList);
