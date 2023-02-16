#!/usr/bin/node

const argv = require('process').argv;

/*
 * findSecondBiggest returns the 2nd
 * largest element from parsed array
 */
function findSecondBiggest (array) {
  let tempA = array[0];
  let tempB = tempA;

  for (const i of array) {
    if (i > tempA) {
      tempA = i;
    }
  }
  for (const i of array) {
    if (i > tempB && i < tempA) {
      tempB = i;
    }
  }
  return tempB;
}
let secongBiggest;
if (argv.length <= 3) {
  secongBiggest = 0;
} else {
  secongBiggest = findSecondBiggest(argv.slice(2).map(item => Number(item)).filter(item => !isNaN(item)));
}
console.log(secongBiggest);
