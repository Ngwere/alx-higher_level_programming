#!/usr/bin/node
const myArgs = process.argv.slice(2);
let result = 0;
function add (a, b) {
  result = a + b;
  return result;
}
if (isNaN(parseInt(myArgs[0])) || isNaN(parseInt(myArgs[1]))) {
  console.log('NaN');
} else {
  console.log(add(parseInt(myArgs[0]), parseInt(myArgs[1])));
}
