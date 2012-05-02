class Dessert
	def initialize(name, calories)
		@food_name = name
		@food_caleories = calories
	end
	def calories # instance method
		@food_caleories # instance var: visible only to this object
	  end
	def calories=(new_amount)  # note method name: like setter
	    @food_caleories = new_amount
	end
	def name
		@food_name
	end
	def name=(new_name)
		@food_name = new_name
	end
	def healthy?
		return @food_caleories < 200
	end
	def delicious?
		return true
	end 
end

class JellyBean < Dessert
	def initialize(name, calories, flavor)
		# YOUR CODE HERE
		@food_name = name
		@food_caleories = calories
		@food_flavor = flavor
	end
	def flavor
		@food_flavor
	end
	def flavor=(new_flavor)
		@food_flavor = new_flavor
	end
	def delicious?
		if @food_flavor == 'black licorice'
			return false
		else
			return true
		end
	end 
end

# jelly = JellyBean.new('jelly bean', 250, 'black licorice')

# print jelly.delicious?
# print jelly.name
# print jelly.flavor