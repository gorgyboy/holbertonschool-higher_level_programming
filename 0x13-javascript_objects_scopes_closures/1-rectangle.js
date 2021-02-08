#!/usr/bin/node
// Defines a class Rectangle with attributes.

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
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
