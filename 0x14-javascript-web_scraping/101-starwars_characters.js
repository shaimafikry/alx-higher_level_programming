#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
// IMPORT THE ARGV
const { argv } = require('node:process');
// The first argument is the movie ID
const filmId = argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
// using function to catch the error if occured and body and response
request.get(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movies = JSON.parse(body);
	let i = 0;
    for (i = 0; i < movies.characters.length; i++) {
      request.get(movies.characters[i], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const chart = JSON.parse(body);
          console.log(chart.name);
        }
      });
    };
  }
});
