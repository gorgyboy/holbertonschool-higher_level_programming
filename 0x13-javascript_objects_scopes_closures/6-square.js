#!/usr/bin/node
// Defines class Square that inherits from Rectangle of 4-rectangle.js.

class Square extends require('./5-square.js') {
  // Prints the rectangle using the character 'c'.
  // If 'c' is undefined, uses 'X'.
  charPrint (c) {
    if (c === undefined) {
      for (let s = 0; s < this.width; s++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let s = 0; s < this.width; s++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

/*
Do not forget to type it as "module.exports", otherwise it doesn't work
when called by require. "module" refers to the current module, which is the
present script and this is like this becuase Node.js conciders each script as
module, so when using "exports", "module" refers to the current script,
as said before.
*/
module.exports = Square;

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');
