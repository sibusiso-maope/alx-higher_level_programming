#!/usr/bin/node
const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < parseInt(process.argv[2]); k++) {
    console.log(lang);
  }
}
