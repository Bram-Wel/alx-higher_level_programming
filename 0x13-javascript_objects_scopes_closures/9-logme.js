#!/usr/bin/node

let no = 0;
exports.logMe = function (item) {
  console.log(`${no}: ${item}`);
  no += 1;
};
