#!/usr/bin/node
function callMeMoby(x, theFunction) {
  let i = 0;
  for (i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
