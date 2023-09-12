#!/usr/bin/node
/*
    func which  printss num arg already printed and the new arg values
    Prototype: exports.logMe = function (item)
    Output format: <number arguments already printed>: <current argument value>
*/

let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};
