#!/usr/bin/node
/*
    scripted got the content of a webpage nd stores it in a file
    when the first arg is the URL request
    secodn arg is the file stored
    file was UTF-8 encoded
    module request used
*/

const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');

function writeFile (nameFile, data) {
  fs.writeFile(nameFile, data, 'utf8', (err) => {
    if (err) {
      return console.error(err);
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    writeFile(fileName, body);
  }
});
