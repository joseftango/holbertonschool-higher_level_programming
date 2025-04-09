#!/usr/bin/node
const x = parseInt(process.argv[2]) || null;
let square = '';
if (x === null) { console.log('Missing size'); } else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    if (i < x - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
