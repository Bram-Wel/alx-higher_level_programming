#!/usr/bin/node
const argv = require('process').argv;

if (argv[2] && argv[3] && argv[4]) {
  const fs = require('fs');
  const f1 = fs.readFileSync(argv[2], 'utf8');
  const f2 = fs.readFileSync(argv[3], 'utf8');
  fs.writeFileSync(argv[4], f1 + f2, 'utf8');
}
