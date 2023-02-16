#!/usr/bin/node

const argv = require('process').argv;

if (!argv[2]) {
  console.log('No Argument');
} else {
  console.log(argv[2]);
}
