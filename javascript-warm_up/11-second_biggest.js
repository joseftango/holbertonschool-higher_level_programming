#!/usr/bin/node
const process = require('process');
const num = process.argv;
const len = num.length;
let greatest = 0;
let wanted = 0;
if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    if (parseInt(num[i]) > greatest) {
      greatest = num[i];
    }
  }
  for (let i = 2; i < len; i++) {
    if (parseInt(num[i]) > wanted && parseInt(num[i]) !== greatest) {
      wanted = num[i];
    }
  }

  console.log(wanted);
}
