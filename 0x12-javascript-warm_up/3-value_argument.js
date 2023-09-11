#!/usr/bin/node
/*
  script printings the first argument into it
*/

const args = process.argv;
if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
