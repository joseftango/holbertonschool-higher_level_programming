#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get({ url, json: true }, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (res.statusCode !== 200) {
    console.error('Failed with status code:', res.statusCode);
  } else {
    console.log(body.title);
  }
});
