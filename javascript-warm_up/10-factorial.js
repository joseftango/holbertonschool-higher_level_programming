#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
if (isNaN(num1)) {
  console.log(num1);
} else {
  console.log(factorial(num1));
}

function factorial (num) {
  if (num === 1) { return 1; }
  return num * factorial(num - 1);
}
