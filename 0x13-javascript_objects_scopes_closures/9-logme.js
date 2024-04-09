#!/usr/bin/node
let narg = 0;
exports.logMe = function (item)
{
	exports.log(narg + ': ' + item);
	narg++;
};
