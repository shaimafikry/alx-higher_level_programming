#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
// IMPORT THE ARGV
const { argv } = require('node:process');
// The first argument is the movie ID
const url = argv[2];
const id = 'people/18/';
const urlPeople = url.replace('films', id);
// console.log(urlPeople)
// using function to catch the error if occured and body and response
request.get(urlPeople, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const charcter = JSON.parse(body);
    // console.log(charcter.name)
    let count = 0;
    charcter.films.forEach(() => {
      count++;
    });
    console.log((count));
  }
});
