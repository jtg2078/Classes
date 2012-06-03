var a = 1;
var x = 2;
var y = 2;

function myfun(x) {
        var a = 3; 
        x = x + y;
        y = x + y;
        var p = function(y,z) {
                var q = function(x,z) {
						console.log('inner')
						console.log('x:'+x)
						console.log('a:'+a)
						console.log('y:'+y)
						console.log('z:'+z)  
                        return x+a*y/z;
                } ;
                return q; 
        } ;
        while (x < y && (x < 10)) {
                if (! (x < y)) {
                        x = x - 1; 
                } else {
                        x = x + 1; 
                } 
                a = a + 1;
        }
		
		console.log('outer');
				console.log('a:'+a);
				console.log('x:'+x);
				console.log('y:'+y);
        return p(a,y); 
}

function myfun1(x) {
        var a = 3; 
        x = x + y;
        y = x + y;
        var p = function(y,z) {
                var q = function(x,z) {
						x = 6
						a = 3
						y = 2
						z = 7
                        return x+a*y/z;
                } ;
                return q; 
        } ;
		// 2
		limit  = 2
		counter  = 0
        while (counter < limit) {
                if (!(x < y)) {
                        x = x - 1; 
                } else {
                        x = x + 1; 
                } 
                a = a + 1;
				counter ++; 
        }
		
        return p(a,y); 
} 
 
var f = myfun(y);
var z = myfun1(y);
console.log( f(6,7) ) ;
console.log( z(6,7) ) ;
