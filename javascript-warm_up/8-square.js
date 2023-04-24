#!/usr/bin/node
const process = require('process');
const size = process.argv[2];
let i = 0;
let j;
if (!isNaN(size)) {
  while (i < size) {
    j = 0;
    while (j < size) {
      process.stdout.write('X');
      j++;
    }
    process.stdout.write('\n');
    i++;
  }
} else {
  console.log('Missing size');
}
