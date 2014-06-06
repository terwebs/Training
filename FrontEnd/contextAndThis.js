var webster = {
	firstName: 'Webster',
	lastName: 'Munoz',
	fullName: function() { return this.firstName + ' ' + this.lastName; }

}

var dan = {
	firstName: 'Dan',
	lastName: 'Wahlin',
}
dan.stolenFullName = webster.fullName;
console.log(dan.stolenFullName());