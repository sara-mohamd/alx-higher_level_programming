#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined)c = 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(`${c}`.repeat(this.width));
    }
  }
}
module.exports = Square;
