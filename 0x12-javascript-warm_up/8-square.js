#!/usr/bin/node

const argv = require('process').argv;
let arg1 = Number(argv[2]);

if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  let temp = arg1;
  while (arg1 > 0) {
    let row = '';
    while (temp > 0) {
      row += 'X';
      temp--;
    }
    temp = Number(argv[2]);
    console.log(row);
    arg1--;
  }
}
