#!/usr/bin/node

const Resu = 'C is fun';
const arg = parseInt(process.argv[2]);
let count;
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}
else {
  for (count = 0; count < arg; count++) {
    console.log(Resu);
  }
}
