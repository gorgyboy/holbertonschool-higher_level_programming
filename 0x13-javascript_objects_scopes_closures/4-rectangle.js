#!/usr/bin/node
// Defines a class Rectangle.

class Rectangle {
  // If w and h are not greater than 0, creates an empty object.
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Prints the rectangle using the character 'X'.
  print () {
    for (let h = 0; h < this.height; h++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Exchanges the width and the height of the rectangle.
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Multiples the width and the height of the rectangle by 2.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

/*
Do not forget to type it as "module.exports", otherwise it doesn't work
when called by require. "module" refers to the current module, which is the
present script and this is like this becuase Node.js conciders each script as
module, so when using "exports", "module" refers to the current script,
as said before.
*/
module.exports = Rectangle;
