#!/usr/bin/node

const argv = require('process').argv;
const arg1 = Number(argv[2]);
const arg2 = Number(argv[3]);

/**
 * add 2 integers and
 * return result
 */
function add (a, b) {
  return a + b;
}

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('NaN');
} else {
  console.log(add(arg1, arg2));
}
