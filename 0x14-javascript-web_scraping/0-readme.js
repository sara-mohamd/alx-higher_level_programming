#!/usr/bin/node
const file = require('file');
file.readFile(`${process.argv[1]}`, 'utf8', (err, data) => {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
