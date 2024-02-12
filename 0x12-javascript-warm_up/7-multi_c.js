#!/usr/bin/node

// prints 3 lines: (like 1-multi_languages.js) but by
// using an array of string and a loop
const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < parseInt(process.argv[2]); k++) {
    console.log(lang);
  }
}
