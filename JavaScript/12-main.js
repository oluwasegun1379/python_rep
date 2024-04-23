#!/usr/bin/node
const addMeMaybe = require("./102-node").addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log("New value: " + nb);
});
