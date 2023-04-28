#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const myfile = process.argv[2]; const mystr = process.argv[3];
fs.writeFile(myfile, mystr, 'utf-8', function (err) {
  if (err) { throw console.log(err); }
});
