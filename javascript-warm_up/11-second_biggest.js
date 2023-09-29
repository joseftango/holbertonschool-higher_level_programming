#!/usr/bin/node
const process = require('process');
const num = process.argv;
if (num.length === 2 || num.length === 3) {
  console.log(0);
} else {
  num.sort((a, b) => a - b);
  console.log(num[num.length - 2]);
}
