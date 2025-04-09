#!/usr/bin/node
const args = process.argv.slice(2);
const myList = args.map(num => parseInt(num));

if (myList.length === 0) { console.log(0); } else if (myList.length === 1) { console.log(1); } else {
  let largest = myList[0];
  for (let i = 0; i < myList.length; i++) {
    if (myList[i] > largest) { largest = myList[i]; }
  }
  console.log(largest);
}
