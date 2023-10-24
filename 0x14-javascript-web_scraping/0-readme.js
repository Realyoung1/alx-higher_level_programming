#!/usr/bin/node
/*
    when first args is the first path
    i make sure the content of the file read utf-8
    th error object was print in case an erro occur
*/

const fs = require('fs');
const nameFile = process.argv[2];

fs.readFile(nameFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
