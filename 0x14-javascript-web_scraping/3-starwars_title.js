#!/usr/bin/node
/*
     Printed the Star Wars movies
     when the first arg is the movie ID
     Star wars API with the endpoint
     https://swapi-api.alx-tools.com/api/films/:id
     module request used
*/

const request = require('request');
const movieID = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
});
