#!/usr/bin/node
/*
  writing a script that pass a message depending on the number of args
*/

const args = process.argv;
if (args.length <= 2) {console.log('No argument');}
else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
