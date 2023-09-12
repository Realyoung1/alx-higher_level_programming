#!/usr/bin/node
/*
     funcs which convert a numb from base 10 to another base passed as args
     Prototype: exports.converter = function (base)
     You are not allowed to import any file
     You are not allowed to declare any new variable (var, let, etc..)

*/

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
