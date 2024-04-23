#!/usr/bin/node
const callMeMoby = require("./101-node").callMeMoby;
callMeMoby(3, function () {
  console.log("C is fun");
});
