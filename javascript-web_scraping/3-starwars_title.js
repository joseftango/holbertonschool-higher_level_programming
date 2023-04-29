#!/usr/bin/node
const process = require('process');
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
const wantedurl = url + id;

request(wantedurl, function (error, response, body) {
  if (error) { throw console.log(error); }
  const obj = JSON.parse(body);
  console.log(obj.title);
});
