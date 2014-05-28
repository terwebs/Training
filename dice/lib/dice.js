var die = {
    size: 6,
	roll: function(){
	   var result = Math.ceil(this.size * Math.random());
	   return result;
	},

	rollString: function() {
		var stringDice = this.roll();

		if(stringDice <= 6 && stringDice >= 1){
			return true;
		}
		return false;

	}
};

exports.die = die;