#!/usr/bin/node
/*
    Square classed that defines squares
    inherited from a Rectangless
    created a charPrint(c) methodings
*/

class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let height = 0; height < this.height; height++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
