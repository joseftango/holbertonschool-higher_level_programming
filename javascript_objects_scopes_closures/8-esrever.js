#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  let i = list.length - 1;
  let j = 0;
  while (i >= 0) {
    revlist[j] = list[i];
    j++;
    i--;
  }
  return revlist;
};
