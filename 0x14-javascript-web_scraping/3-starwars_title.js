#!/usr/bin/node
// const request = require('request');
// request(`https://swapi-api.alx-tools.com/api/films/:${process.argv[2]}`, (err, res, body) => {
//   if (err) {
//     console.log(err);
//   } else if (res.statusCode === 200) {
//     // const json = ;
//     console.log((JSON.parse(body)).title);
//   } else {
//     console.log(`Error: ${res.statusCode}`);
//   }
// });

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
