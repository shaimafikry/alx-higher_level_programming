#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const request = require('request');
// IMPORT THE ARGV
const { argv } = require('node:process');
// The first argument is the url
const url = argv[2];
// dict of users
const users = {};
// using function to catch the error if occured and body and response
request.get(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    data.forEach((element) => {
      const user = element.userId;
      data.forEach((loopElement) => {
        if (user === loopElement.userId &&
            loopElement.completed === true) {
          count++;
        }
      });
      users[user] = count;
      count = 0;
    });
    console.log(users);
  }
});
