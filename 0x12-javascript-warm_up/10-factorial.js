#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const [,, arg] = process.argv;
const integer = parseInt(arg);

console.log(factorial(integer));
