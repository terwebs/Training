var die = require("../lib/dice").die;

exports["Can verify if the roll result is a number < 6"]= function(test){
	var result = die.rollString();

	test.equal(result, true);
	test.done();
};

exports["Roll returns an integer between 1 and 6"] = function(test){
	var result = die.roll();

	test.ok((result <=6 && result >=1), 'Result should be between 1 and 6');
	test.done();
};

// Returns a random integer between min and max
// Using Math.round() will give you a non-uniform distribution!
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};