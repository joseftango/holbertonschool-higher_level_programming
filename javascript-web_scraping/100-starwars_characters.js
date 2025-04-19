#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request.get({ url, json: true }, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (res.statusCode !== 200) {
    console.error('Failed with status code:', res.statusCode);
  } else {
    for (const ch of body.characters) {
      request.get({ url: ch, json: true }, (e, r, b) => {
        if (e) {
          console.error('Error:', e);
        } else if (r.statusCode !== 200) {
          console.error('Failed: ', r.statusCode);
        } else {
          console.log(b.name);
        }
      });
    }
  }
});
