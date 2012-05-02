class Numeric
	@@currencies = {'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019, 'dollar' => 1.0}
	def method_missing(method_id, *arguments, &block)
		if method_id.to_s == 'in'
			singular_currency = arguments.first.to_s.gsub( /s$/, '')
			if @@currencies.has_key?(singular_currency)
				if(singular_currency == 'dollar' )
					self * @@currencies[singular_currency]
				else
					self / @@currencies[singular_currency]
				end
			else	
				super
			end
		else
			singular_currency = method_id.to_s.gsub( /s$/, '')
			if @@currencies.has_key?(singular_currency)
				self * @@currencies[singular_currency]
			else
				super
			end
		end
	end
end

class String
	def method_missing(method_id, *arguments, &block)
		if method_id.to_s == 'palindrome?'
			cleaned = self.to_s.downcase.gsub(/[^a-z]/,'')
			return cleaned == cleaned.reverse
		else
			super
		end
	end
end

module Enumerable
	def method_missing(method_id, *arguments, &block)
		if method_id.to_s == 'palindrome?'
			b = self.reverse_each
			passed = true
			self.each do |element|
				if(element != b.next)
					passed = false
					return passed
				end
			end
			passed
		else
			super
		end
	end
end

#print 5.rupees.in(:yens)

#print "abccba".palindrome?

#print 5.dollars.in(:euros)

#print "abc".class

#print 2.0.class
#p [[1,2],[1,2]].palindrome?

#p [1,2,3,2,1,9].palindrome?


