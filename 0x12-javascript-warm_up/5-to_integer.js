#!/usr/bin/node
// parseInt-I
const Int = parseInt(process.argv[2]);
if (isNaN(Int)) {
  console.log('Not a number');
}
else {
  console.log(`My number: ${Int}`);
}
