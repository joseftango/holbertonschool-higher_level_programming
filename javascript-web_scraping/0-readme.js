#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const myfile = process.argv[2];
fs.readFile(myfile, 'utf-8', function read (err, data) {
  if (err) {
    throw console.log(err);
  }
  process.stdout.write(data);
});
