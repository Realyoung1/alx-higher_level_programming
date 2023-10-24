#!/usr/bin/node
/*
    printed characters of a Star Wars movie
    where the first agr is the Movie ID -
    diplsyed character anem by line
    used the  Star wars API
    module request used
*/

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    for (const character of jsonBody.characters) {
      request(character, function (errorC, responseC, bodyC) {
        if (errorC) {
          console.log('code:', response.statusCode);
        }
        console.log(JSON.parse(bodyC).name);
      });
    }
  }
});
