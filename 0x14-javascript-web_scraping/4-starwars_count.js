#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
// IMPORT THE ARGV
const { argv } = require('node:process');
// The first argument is the movie ID
const url = argv[2];
request.get(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body);
    let count = 0;
    let i = 0;
    let m = 0;
    for (i = 0; i < (films.results).length; i++) {
      for (m = 0; m < films.results[i].characters.length; m++) {
        if (films.results[i].characters[m].includes(18)) {
          count++;
        }
      }
    }
    console.log((count));
  }
});
