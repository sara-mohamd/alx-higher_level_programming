#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (!err) {
    const result = JSON.parse(body).results;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
