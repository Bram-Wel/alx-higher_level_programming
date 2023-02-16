#!/usr/bin/node

const argv = require('process').argv;
const arg1 = Number(argv[2]);
let fact;

/**
 * factorial of argument 1
 * return result
 */
function factorial (arg) {
  if (arg > 0) {
    return arg * factorial(--arg);
  }
  return 1;
}

if (isNaN(arg1)) {
  fact = 1;
} else {
  fact = factorial(arg1);
}
console.log(fact);
