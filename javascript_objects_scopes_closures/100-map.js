#!/usr/bin/node
const list = require('./100-data').list;
let newli = [];
newli = list.map(function (el, index) {
  return el * index;
});
console.log(list);
console.log(newli);
