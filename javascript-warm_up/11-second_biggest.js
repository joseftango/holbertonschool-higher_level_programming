#!/usr/bin/node
const process = require('process');
const num = process.argv;
const len = num.length;
let greatest = 0;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    if (parseInt(num[i]) > greatest) {
      greatest = num[i];
    }
  }
  console.log(greatest);
}
