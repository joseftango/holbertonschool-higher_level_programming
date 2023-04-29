#!/usr/bin/node
const process = require('process');
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) { throw console.log(error); }
  fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) { throw console.log(err); }
  });
});
