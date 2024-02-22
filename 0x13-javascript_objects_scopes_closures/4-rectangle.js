#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      console.log('Invalid dimensions for the rectangle.');
      return;
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    if (!this.width || !this.height) {
      console.log('Invalid dimensions for the rectangle.');
      return;
    }

    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    if (!this.width || !this.height) {
      console.log('Invalid dimensions for the rectangle.');
      return;
    }

    this.width *= 2;
    this.height *= 2;
  }
};
