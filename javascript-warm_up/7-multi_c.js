#!/usr/bin/node
const args = process.argv.slice(2);
const count = parseInt(args[0]);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  let output = '';
  for (let i = 0; i < count; i++) {
    output += 'C is fun\n';
  }
  if (output) {
    console.log(output.trim());
  }
}
