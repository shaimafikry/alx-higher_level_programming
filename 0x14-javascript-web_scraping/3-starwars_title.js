#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
// IMPORT THE ARGV
const { argv } = require('node:process');
// The first argument is the movie ID
const filmId = argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
// using function to catch the error if occured and body and response
request.get(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log((movie.title));
  }
});
