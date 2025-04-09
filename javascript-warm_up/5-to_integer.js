#!/usr/bin/node
const args = process.argv.slice(2);
const ar = parseInt(args[0]) || null;
if (ar === null) { console.log('Not a Number'); } else { console.log(ar); }
