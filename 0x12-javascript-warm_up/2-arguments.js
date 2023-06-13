#!/usr/bin/node

const argLen = process.argv.length;
if (argLen - 2 === 0){
  console.log('No argument');
}else if (argLen - 2 === 1){
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
