function gcd(a,b) {
    //Write Code Here
	/*
	if(a == b)
		return a;
	else if(a > b)
		return gcd(a-b, b);
	else
		return gcd(a, b-a);
		*/
	if (b == 0) 
	{
		return a;
	}
	else
	{
		return gcd(b, a % b);
	}
		
}

console.log(gcd(24,8) == 8);
console.log(gcd(1362, 1407)); // Empress Xu (Ming Dynasty) wrote biographies
console.log(gcd(1875, 1907)); // Qiu Jin, feminist, revolutionary, and writer
console.log(gcd(45,116)); // Ban Zhao, first known female Chinese historian