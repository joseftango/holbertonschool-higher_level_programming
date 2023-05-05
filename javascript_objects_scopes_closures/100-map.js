#!/usr/bin/node
const list = require('./100-data').list;
const newli = [];
list.map(function (el, index) {
  newli[index] = el * index;
});
console.log(list);
console.log(newli);
