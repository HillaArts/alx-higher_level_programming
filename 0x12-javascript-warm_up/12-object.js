#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

(() => {
  Object.defineProperty(myObject, 'value', {
    writable: true,
    configurable: true,
    enumerable: true,
    value: 89
  });
})();

console.log(myObject);
