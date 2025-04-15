#!/usr/bin/node
const S = require('./5-square');

module.exports = class Square extends S {
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
