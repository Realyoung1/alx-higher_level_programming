#!/usr/bin/node
/*
     it displaed  the status code GET request
     when the first args is the url GET
     we have status code printed in code: <status code>
     module equest was used
*/

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    console.log('code:', response.statusCode);
  }
});
