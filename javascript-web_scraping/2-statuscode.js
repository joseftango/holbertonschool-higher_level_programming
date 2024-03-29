#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestSettings = {
  method: 'HEAD',
  url: process.argv[2]
};

request(requestSettings, function (error, response, body) {
  if (error) { throw console.log(error); }
  console.log(`code: ${response.statusCode}`);
});
