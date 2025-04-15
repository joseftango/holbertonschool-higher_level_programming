#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}

console.log(newDict);
