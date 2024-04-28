#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (process.argv[2] > 0) {
  for (let i = 0; i < process.argv[2]; i++) {
    let temp = '';
    for (let j = 0; j <= process.argv[2]; j++) { temp += 'x'; }
    console.log(temp);
  }
}
