#!/usr/bin/node

// prints a square
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let k = 0; k < parseInt(process.argv[2]); k++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
