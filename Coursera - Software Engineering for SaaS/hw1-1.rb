def palindrome?(string) # your code here
	cleaned = string.to_s.downcase.gsub(/[^a-z]/,'')
	return cleaned == cleaned.reverse
end

# palindrome?("A man, a plan, a canal -- Panama") #=> true 
# palindrome?("Madam, I'm Adam!") # => true 
# palindrome?("Abracadabra") # => false (nil is also ok)

# print palindrome?("A man, a plan, a canal -- Panama")
# print palindrome?("Madam, I'm Adam!")
# print palindrome?("Abracadabra")
# print palindrome?("jason")
# print palindrome?("bob")

def count_words(string) # your code here
	counter = {}
	cleaned = string.to_s.downcase
	cleaned.gsub(/\b\w+/).each do |token|
		# print token
		# print ","
		if counter.has_key?(token)
			counter[token] += 1
		else
			counter[token] = 1
		end
	end
	return counter
end

# print count_words("wat, --- a is, .goingeasdon")

#print count_words("A man, a plan, a canal -- Panama") # => {'a' => 3, 'man' => 1, 'canal' => 1, 'panama' => 1, 'plan' => 1}
#print count_words "Doo bee doo bee doo" # => {'doo' => 3, 'bee' => 2}