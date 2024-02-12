#!/usr/bin/node

// executes a function x amount of times
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
