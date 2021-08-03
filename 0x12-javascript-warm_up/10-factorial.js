#!/usr/bin/node
/* Script that computes and prints a factorial */
const number = parseInt(process.argv[2]);

function recursion (number) {
  if (number === 1) {
    return 1;
  } else {
    return number * recursion(number - 1);
  }
}

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(recursion(number));
}
