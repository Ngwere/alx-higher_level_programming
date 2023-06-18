#!/usr/bin/node
module.exports = class Rectangle{
	constructor (w, h) {
		if (w > 0 && h >0) { [this.width = w, this.height = h] = [w, h];}
	}

	print() {
		for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
	}

	rotate() {
		const constant = this.height;
		this.height = this.width;
		this.width = constant;
	}

	double() {
		[this.width, this.height] = [this.width * 2, this.height * 2];
	}
};
