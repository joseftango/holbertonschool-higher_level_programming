#!/usr/bin/node
const args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else {
  for (const ar of args) {
    console.log(ar);
  }
}
