#!/usr/bin/node
const args = process.argv.slice(2);
const myList = args.map(num => parseInt(num)).sort((a, b) => b - a);

if (myList.length === 0 || myList.length === 1) { console.log(0); } else {
  const secondLargest = myList[1];
  console.log(secondLargest);
}
