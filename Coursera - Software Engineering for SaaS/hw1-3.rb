def combine_anagrams(words) 
	# <YOUR CODE HERE>
	# sort each word
	# make the sorted word as key of that word
	# put them in the hash
	keeper = {}
	words.each do |word|
		sorted = word.downcase.chars.sort.join
		if keeper.has_key?(sorted)
			keeper[sorted] << word
		else
			keeper[sorted] = [word]
		end
	end
	result = []
	keeper.each_pair do |key,val|
		result << val
	end
	return result
end

# print combine_anagrams(['cars', 'for', 'potatoes', 'racs', 'four','scar', 'creams', 'scream'])