#!/usr/bin/node
const x = parseInt(process.argv[2]) || null;
if (x === null) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) { console.log('C is fun'); }
}
