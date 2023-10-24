#!/usr/bin/node
/*
     when first args is the first path
     when the second args was the string
     i make sure the content of the file read utf-8
     th error object was print in case an erro occur
*/

const fs = require('fs');
const nameFile = process.argv[2];
const str = process.argv[3];

fs.writeFile(nameFile, str, 'utf8', (err) => {
  if (err) {
    return console.error(err);
  }
});
