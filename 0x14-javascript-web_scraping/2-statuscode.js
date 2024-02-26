#!/usr/bin/node
const request = require('request');
request.get(process.argv[2]).on('response', res => {
  console.log(`code: ${res.statusCode}`);
});
