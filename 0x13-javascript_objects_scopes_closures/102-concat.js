#!/usr/bin/node
/*
    scripted that concats two files.
    The first argument is the file path of the first source file
    The second argument is the file path of the second source file
    The third argument is the file path of the destination
*/
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
// Asynchronous read
function readfiles (nameFile) {
  return fs.readFileSync(nameFile);
}

function writefiles (nameFile, data) {
  fs.writeFile(nameFile, data, (err) => {
    if (err) {
      return console.error(err);
    }
  });
}
let dataFile = '';
dataFile = readfiles(file1);
dataFile += readfiles(file2);
writefiles(file3, dataFile);
