#!/usr/bin/node

const SquareI = require('./5-square.js');
class Square extends SquareI {
  charPrint (c) {
    return this.print(c);
  }
}
module.exports = Square;
