#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) { throw console.log(error); }
  const obj = JSON.parse(body);
  let count;
  const res = {};
  for (let i = 0; i < obj.length; i++) {
    if (res[`${obj[i].userId}`] === undefined) {
      count = 0;
    }
    if (obj[i].completed === true) { count++; }
    res[`${obj[i].userId}`] = count;
  }
  console.log(res);
});
