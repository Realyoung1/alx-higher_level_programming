#!/usr/bin/node
/*
   Square classed that defines squares
    inherited from the Rectangless
*/

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
