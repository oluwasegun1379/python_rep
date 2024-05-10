#!/usr/bin/node
const oldSquare = require("./5-node");
class Square extends oldSquare {
  charPrint(c) {
    if (c === undefined) {
      c = "X";
    }
    for (let i = 0; i < this.height; i++) {
      let x = "";
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
}
module.exports = Square;
