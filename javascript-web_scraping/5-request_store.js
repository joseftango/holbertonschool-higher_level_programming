#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const f = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed with status code:', response.statusCode);
  } else {
    fs.writeFile(f, body, (err) => {
      if (err) { console.log(err); }
    });
  }
});
