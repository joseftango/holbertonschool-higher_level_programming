#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];
fs.readFile(fp, 'utf-8', (err, content) => {
  if (err) { console.log(err); } else { console.log(content); }
});
