#!/usr/bin/node
/*
 this funcs has executed x times funct
*/

const callMeMoby = function (x, theFunction) {
  for (let times = x; times > 0; times--) {
    theFunction();
  }
};

exports.callMeMoby = callMeMoby;
