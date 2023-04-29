#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) { throw console.log(error); }
  const obj = JSON.parse(body);
  let count = 0;
  for (const item in obj.results) {
    const chars = obj.results[item].characters;
    for (const i in chars) {
      if (chars[i].includes('18')) { count++; }
    }
  }
  console.log(count);
});
