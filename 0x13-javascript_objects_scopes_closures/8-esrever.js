#!/usr/bin/node
/*
    this is the func which returned the reverse version of list
    Prototype: exports.esrever = function (list)
    not allowed to use the built in method
*/
exports.esrever = function (list) {
  const revList = [];
  for (let index = list.length - 1; index >= 0; index--) {
    revList.push(list[index]);
  }
  return revList;
};
