#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (isNaN(parseInt(myArgs[0]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < parseInt(myArgs[0]); i++) {
    row = '';
    for (j = 0; j < parseInt(myArgs[0]); j++) {
      row += 'X';
    }
    console.log(row);
  }
}
