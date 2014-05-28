var die = require("../lib/dice").die;

exports["Can verify if the roll result is a number < 6"]= function(test){
	var result = die.rollString();

	test.equal(result, true);
	test.done();
};