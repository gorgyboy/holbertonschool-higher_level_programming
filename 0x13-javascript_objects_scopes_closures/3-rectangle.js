#!/usr/bin/node
// Defines a empty class Rectangle.

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      console.log('X'.repeat(this.width));
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
module.exports = Rectangle;
