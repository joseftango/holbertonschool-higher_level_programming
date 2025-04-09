#!/usr/bin/node
const args = process.argv.slice(2);
const myList = args.map(num => parseInt(num)).sort((a, b) => b - a);

if (myList.length === 0) { console.log(0); } else if (myList.length === 1) { console.log(1); } else {
  const secondLargest = myList[1];
  console.log(secondLargest);
}
