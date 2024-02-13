#!/usr/bin/node

(() => {
  const args = process.argv.slice(2).map(Number);

  if (args.length <= 1) {
    console.log(0);
  } else {
    let max = Number.MIN_SAFE_INTEGER;
    let secondMax = Number.MIN_SAFE_INTEGER;

    args.forEach((num) => {
      if (num > max) {
        secondMax = max;
        max = num;
      } else if (num > secondMax && num !== max) {
        secondMax = num;
      }
    });

    if (secondMax === Number.MIN_SAFE_INTEGER) {
      console.log(0);
    } else {
      console.log(secondMax);
    }
  }
})();
