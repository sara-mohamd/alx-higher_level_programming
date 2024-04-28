#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('x'.repeat(process.argv[2]));
  }
}
