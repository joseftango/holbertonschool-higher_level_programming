#!/usr/bin/node
const args = process.argv;
const len = args.length;
if (len === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < len; i++) { console.log(args[i]); }
}
