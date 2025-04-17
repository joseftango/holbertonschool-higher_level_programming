#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];
const str = process.argv[3] + '\n';

fs.writeFile(fp, str, (err, data) => {
  if (err) { console.log(err); }
});
