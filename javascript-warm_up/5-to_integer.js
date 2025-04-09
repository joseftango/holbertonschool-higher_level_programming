#!/usr/bin/node
const args = process.argv.slice(2);
const ar = parseInt(args[0]) || null;
if (ar === null) { console.log('Not a number'); } else { console.log('My number: ' + ar); }
