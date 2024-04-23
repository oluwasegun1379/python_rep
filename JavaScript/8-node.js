#!/usr/bin/node
const arg = process.argv;
let j = 0;
if (!arg[2] || isNaN(parseInt(arg[2]))) {
  console.log("Missing size");
} else {
  let x = parseInt(arg[2]);
  for (j = 0; j < x; j++) {
    console.log("x".repeat(x));
  }
}
