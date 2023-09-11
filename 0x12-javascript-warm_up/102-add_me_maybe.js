#!/usr/bin/node
/*
   func that incremented and called a function
*/

const addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};

exports.addMeMaybe = addMeMaybe;
