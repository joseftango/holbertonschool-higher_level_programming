#!/usr/bin/node
const process = require('process');
const arg = process.argv;
let res = 0;

if (arg.length === 2 || arg[2] === undefined) console.log(0)
else {
for (let i=2; i < arg.length; i++) {
	if (res < arg[i]) {
		res = arg[i];
	}
}
console.log(res)
}
