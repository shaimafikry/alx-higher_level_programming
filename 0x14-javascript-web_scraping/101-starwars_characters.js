#!/usr/bin/node
// still cant get the difference between it and the prev
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
    const movie = JSON.parse(body);
    const movieChars = movie.characters;
    for (const char of movieChars) {
      request.get(char, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const charNames = JSON.parse(body);
          console.log(charNames.name);
        }
      });
    }
  }
});
