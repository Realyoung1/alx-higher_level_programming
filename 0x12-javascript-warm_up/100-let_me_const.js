#!/usr/bin/node
/*
 filed that modifies the value of myVar to 333.
*/

var insta = (function () {
  myVar = 333;
})();

module.exports = insta;
