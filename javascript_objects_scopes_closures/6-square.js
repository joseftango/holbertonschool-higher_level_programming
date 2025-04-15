#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let MyRectangle = '';
    if (c === undefined) { c = 'X'; }

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        MyRectangle += c;
      }
      if (i < this.height - 1) {
        MyRectangle += '\n';
      }
    }

    console.log(MyRectangle);
  }
};
