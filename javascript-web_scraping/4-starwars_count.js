#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get({ url, json: true }, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (res.statusCode !== 200) {
    console.error('Failed with status code:', res.statusCode);
  } else {
    let count = 0;
    for (const movie of body.results) {
      for (const char of movie.characters) {
        if (char.endsWith('/18/')) {
          count += 1;
          break;
        }
      }
    }
    console.log(count);
  }
});
