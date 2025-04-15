#!/usr/bin/node
exports.esrever = function (list) {
  const RevLi = [];
  let i = list.length - 1;
  while (i >= 0) {
    RevLi.push(list[i]);
    i--;
  }
  return RevLi;
};
