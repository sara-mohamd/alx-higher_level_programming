#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/:${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    // const json = ;
    console.log((JSON.parse(body)).title);
  } else {
    console.log(`Error: ${res.statusCode}`);
  }
});
