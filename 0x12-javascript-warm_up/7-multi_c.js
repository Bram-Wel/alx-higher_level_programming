#!/usr/bin/node

const argv = require('process').argv;
let arg1 = Number(argv[2]);

if (isNaN(arg1)) {
  console.log('Missing number of occurences');
} else {
  while (arg1 > 0) {
    console.log('C is fun');
    arg1--;
  }
}
