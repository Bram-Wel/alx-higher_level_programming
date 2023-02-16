#!/usr/bin/node

const argv = require('process').argv;
const arg1 = Number(argv[2]);

if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg1}`);
}
