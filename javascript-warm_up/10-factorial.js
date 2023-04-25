#!/usr/bin/node
const process = require('process');
const num = process.argv[2];
let res = 0;
function fact (x) {
  if (isNaN(x)) {
    return 1;
  }
  x = parseInt(x);
  if ((x === 1 || x === 0) || x === null) {
    return 1;
  }
  return x * fact(x - 1);
}

res = fact(num);
console.log(res);
