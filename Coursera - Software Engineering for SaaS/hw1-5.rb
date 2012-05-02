class Class
 
  def attr_accessor_with_history(attr_name)
    attr_name = attr_name.to_s
    attr_hist_name = attr_name+'_history'
 
    #getter
    self.class_eval("def #{attr_name};@#{attr_name};end")
 
    #setter
    self.class_eval %Q{
      def #{attr_name}=(value)
        if #{attr_name} == nil then      
  			@#{(attr_name + "_history")} = Array.new
  			@#{(attr_name + "_history")}.push(nil)
		end
 
		@#{attr_name} = value
		@#{(attr_name + "_history")}.push(value)
      end
 
      def #{attr_hist_name};@#{attr_hist_name};end
	}
  end
end

class Foo
	attr_accessor_with_history :bar
end

f = Foo.new
f.bar = 1
f.bar = 2
#print f.bar_history # => if your code works, should be [nil,1,2]

f = Foo.new
f.bar = 1
f.bar = 2
f = Foo.new
f. bar = 4
print f.bar_history
